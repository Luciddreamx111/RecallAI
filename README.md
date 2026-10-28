# RecallAI 📚

**Turn study notes into an AI-powered practice quiz.**

RecallAI is a simple AI study assistant that transforms pasted study notes into five multiple-choice questions, each with four options, the correct answer, and a short explanation.

## ✨ Features

- Generates 5 multiple-choice questions from study notes
- Provides four options for each question
- Includes answers and brief explanations
- Uses the supplied notes as context
- Simple, beginner-friendly web interface

## 🛠️ Technology Stack

- Python
- Flask
- Nebius Token Factory API
- NVIDIA Nemotron model
- OpenAI-compatible Python client
- HTML and CSS

## ⚙️ How It Works

1. The user pastes study notes into the web interface.
2. Flask receives the submitted notes.
3. RecallAI sends the notes and quiz-generation instructions to the configured model through the Nebius API.
4. The model generates five multiple-choice questions with answers and explanations.
5. The quiz appears on the webpage.

## 🚀 Run Locally

1. Install Python 3.
2. Clone this repository and open its folder in Terminal.
3. Create and activate a virtual environment.
4. Install the required packages:

   `pip install -r requirements.txt`

5. Create a `.env` file containing your Nebius API key:

   `NEBIUS_API_KEY=your_api_key_here`

6. Start the application:

   `python3 app.py`

7. Open `http://127.0.0.1:5000` in your browser.

## 🔐 Security

Keep your API key private. Store it in `.env` and never commit that file to GitHub.

## 🎯 Purpose

RecallAI aims to make active recall easier by helping learners turn their own notes into quick practice quizzes.

## 📌 Project Status

Working prototype. Built as a hackathon project.

## 📄 License

MIT License
