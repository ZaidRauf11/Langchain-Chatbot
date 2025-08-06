import os
import streamlit as st
import streamlit.components.v1 as components
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI


load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    google_api_key=GOOGLE_API_KEY
)

# Session states
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

st.set_page_config(page_title="🧠 Langchain Gemini Chatbot", layout="wide")
st.title("🌐 AI Chat Assistant (Langchain + Gemini)")

# Choose Mode
mode = st.selectbox("Choose Chatbot Mode", ["Default", "Math Tutor", "Doctor", "Travel Guide","Grammar Fixer", "Summarizer" , "Quiz Generator"])

# Fixed system prompts
system_prompts = {
    "Default": "You are a helpful assistant.",
    "Math Tutor": "You are a math expert. Answer in a step-by-step logical way.",
    "Doctor": "You are a medical assistant. Always mention this is not medical advice.",
    "Travel Guide": "You are a travel expert helping people explore new places.",
    "Grammar Fixer": "You are a grammar expert. Correct the grammar of any input sentence and suggest improvements.",
    "Summarizer": "You summarize long text into concise points.",
    "Quiz Generator": "Generate a short multiple choice quiz on a given topic."
}

# Use fixed prompt based on mode
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompts[mode]),
        ("human", "Question: {question}")
    ]
)

input_text = st.text_input("✍️ Enter your question/input:")
output_parser = StrOutputParser()
chain = prompt | llm | output_parser

if st.button("🔁 Ask/Run") and input_text:
    response = chain.invoke({"question": input_text})
    st.session_state.chat_history.append({"user": input_text, "bot": response})

# Suggested follow-up
if input_text:
    st.markdown("---")
    st.markdown("### 💡 Suggested Follow-ups:")
    st.button("Can you explain further?")
    st.button("Give an example")
    st.button("What are the real-world uses?")
    
# Show the most recent response just below suggestions
if st.session_state.chat_history:    
    last_response = st.session_state.chat_history[-1]['bot']
    st.markdown("### 🤖 AI Response")
    st.markdown(f"**{last_response}**", unsafe_allow_html=True)
    # st.code(last_response, language='markdown')
    

# AI tools section
st.markdown("---")
st.subheader("💡 AI Assistant Tools")


with st.expander("🧭 Career Counseling Tool"):
    career_input = st.text_input("Describe your interests, skills, or goals")
    if st.button("🎯 Get Career Advice") and career_input:
        response = chain.invoke({"question": f"Suggest suitable careers for someone with these interests or skills: {career_input}"})
        st.success(response)

with st.expander("📄 Cover Letter Generator"):
    job_info = st.text_area("Enter job title and your background")
    if st.button("✍️ Generate Cover Letter") and job_info:
        response = chain.invoke({"question": f"Write a professional cover letter for this: {job_info}"})
        st.success(response)

with st.expander("🧘 Mental Wellness Tips"):
    feeling = st.text_input("How are you feeling today?")
    if st.button("💡 Get Tip") and feeling:
        response = chain.invoke({"question": f"I'm feeling {feeling}. Give a positive, supportive tip (not medical advice)."})
        st.success(response)

with st.expander("🎲 Random Fact Generator"):
    if st.button("🎉 Surprise Me"):
        response = chain.invoke({"question": "Give me a surprising fact"})
        st.success(response)

with st.expander("🍽️ Recipe Generator"):
    ingredients = st.text_input("Enter available ingredients or a craving")
    if st.button("👨‍🍳 Get Recipe") and ingredients:
        response = chain.invoke({"question": f"Suggest a recipe using: {ingredients}"})
        st.success(response)

# Show chat history
st.markdown("---")
st.subheader("📝 Chat History")

for i, msg in enumerate(st.session_state.chat_history[::-1]):
    with st.expander(f"👤 You: {msg['user']}"):
        st.markdown("🧠 Bot Response:")
        st.code(msg['bot'], language='markdown')
        st.download_button("⬇️ Download Response", data=msg['bot'], file_name="response.txt", key=f"download_{i}")








































