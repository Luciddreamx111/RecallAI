from dotenv import load_dotenv
load_dotenv()



import os
from flask import Flask, request, render_template_string
from openai import OpenAI

app = Flask(__name__)

client = OpenAI(
    base_url="https://api.tokenfactory.nebius.com/v1/",
    api_key=os.environ.get("NEBIUS_API_KEY", "")
)

MODEL = "nvidia/Nemotron-3.5-Super-VL"

PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>RecallAI</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        body { font-family: Arial; max-width: 760px; margin: 40px auto;
               padding: 20px; background: #f4f5fb; color: #222; }
        h1 { color: #5146d8; }
        textarea { width: 100%; height: 220px; padding: 12px;
                   box-sizing: border-box; border: 1px solid #ccc;
                   border-radius: 10px; font-size: 16px; }
        button { background: #5146d8; color: white; border: 0;
                 padding: 12px 20px; border-radius: 8px; cursor: pointer; }
        .result { background: white; padding: 20px; border-radius: 10px;
                  margin-top: 20px; white-space: pre-wrap; }
        .error { color: #b00020; }
    </style>
</head>
<body>
    <h1>RecallAI 📚</h1>
    <p>Turn your study notes into a practice quiz using AI.</p>
    <form method="post">
        <textarea name="notes" required
        placeholder="Paste your study notes here...">{{ notes }}</textarea>
        <p><button type="submit">Generate my quiz</button></p>
    </form>
    {% if result %}
        <div class="result">{{ result }}</div>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    notes = ""
    result = ""

    if request.method == "POST":
        notes = request.form.get("notes", "").strip()

        if not notes:
            result = "Please paste some study notes first."
        elif not client.api_key:
            result = "API key missing. Check your .env configuration."
        else:
            try:
                response = client.chat.completions.create(
                    model=MODEL,
                    messages=[
                        {
                            "role": "system",
                            "content": (
                                "You are RecallAI, a study assistant. "
                                "Use only the supplied notes. Create 5 "
                                "numbered multiple-choice questions, each "
                                "with 4 options, the correct answer, and "
                                "a short explanation. If the notes lack "
                                "enough information, say so honestly."
                            )
                        },
                        {"role": "user", "content": notes}
                    ],
                    max_tokens=1200,
                    temperature=0.4
                )
                result = response.choices[0].message.content or "No quiz returned."
            except Exception as e:
                result = f"AI request failed: {e}"

    return render_template_string(PAGE, notes=notes, result=result)

if __name__ == "__main__":
    app.run(debug=True)
