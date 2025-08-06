# 🧠 LangChain + Gemini Streamlit Chatbot

A multi‑mode AI Chat Assistant built with **LangChain** and **Google Gemini 2.0 Flash**, deployed as a **Streamlit** app for real‑time, interactive user conversations.

---

## 🔧 Features

- 🎭 Multiple chatbot roles:
  - Math Tutor
  - Career Counselor
  - Grammar Fixer
  - Doctor (not medical advice)
  - Travel Guide
  - Surprise Me!
  - Summarizer
  - Quiz Generator

- 🛠 Built‑in utility tools accessible via expandable sections:
  - Cover Letter Generator
  - Career Advice
  - Mental Wellness Tips
  - Random Fact / Quiz Generator
  - Recipe Suggestion

- 💬 Real-time chat input with response output
- 🧾 Chat history stored in session with optional download
- 🎨 Smooth Streamlit UI for a clean user experience

---

## 🗂️ Project Structure

CHATBOT_PROJECT/
├── langchain_chatbot.py # Main Streamlit app code
├── requirements.txt # Dependency list
└── .env # Holds your GOOGLE_API_KEY (not uploaded to GitHub)

---

## 🛠️ Getting Started — Local Run

1. Clone the repo:
   ```bash
   git clone https://github.com/ZaidRauf11/Langchain-Chatbot.git
   cd Langchain-Chatbot


Create and activate a virtual environment:

python -m venv venv
source venv/bin/activate  # on Windows use: venv\Scripts\activate


Install dependencies:

pip install -r requirements.txt


Create a .env file with:

GOOGLE_API_KEY=your_google_gemini_api_key


Run the app:

streamlit run langchain_chatbot.py
Open your browser to http://localhost:8501 to interact with the chatbot.


🧠 How It Works

Load API Key from .env using python-dotenv.

Initialize Gemini-2.0 Flash model via ChatGoogleGenerativeAI.

Prompt templates configured via LangChain’s ChatPromptTemplate.

User input is routed through chain.invoke(...) and results are parsed with StrOutputParser.

Chat history is stored in st.session_state.chat_history for display and export.

UI widgets allow mode selection, follow-up prompts, and access to built-in tool sections.


📦 Dependencies

Listed in requirements.txt:
streamlit
langchain-core
langchain-google-genai
python-dotenv


📌 Future Enhancements

🗃️ Enable file upload and document-based RAG (Retrieval Augmented Generation)

🤖 Integrate vector store for knowledge-based chat

🎛️ Add user authentication and personalization

🎨 UI enhancements, dashboard customization, and more modes

🤝 Feedback & Collaboration
I’m open to suggestions, bug fixes, and feature ideas. Feel free to:

⭐ Star the repo

🐞 Submit issues or pull requests

💬 Reach out for collaboration on similar AI‑driven projects

📛 License
Open‑source and free to use — feel free to fork and build on top of this! 🧩

Made by Zaid Rauf | AI Enthusiast, LangChain & Gemini Developer
GitHub: ZaidRauf11/Langchain-Chatbot

---

This README covers:

- A descriptive overview
- Live demo link & GitHub link
- Features and usage
- Local installation & deployment instructions
- Project structure
- Notes for future improvements


   



