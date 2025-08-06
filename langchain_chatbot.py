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
mode = st.selectbox("Choose Chatbot Mode", ["Default", "Math Tutor", "Doctor", "Travel Guide","Career Counselor","Grammar Fixer", "Summarizer", "Surprise Me", "Quiz Generator"])

# Fixed system prompts
system_prompts = {
    "Default": "You are a helpful assistant.",
    "Math Tutor": "You are a math expert. Answer in a step-by-step logical way.",
    "Doctor": "You are a medical assistant. Always mention this is not medical advice.",
    "Travel Guide": "You are a travel expert helping people explore new places.",
    "Grammar Fixer": "You are a grammar expert. Correct the grammar of any input sentence and suggest improvements.",
    "Summarizer": "You summarize long text into concise points.",
    "Surprise Me": "Give a random interesting fact or trivia.",
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

# if st.button("🔁 Ask/Run") and input_text:
#     response = chain.invoke({"question": input_text})
#     st.session_state.chat_history.append({"user": input_text, "bot": response})
    

# # Suggested follow-up
# if input_text:
#     st.markdown("---")
#     st.markdown("### 💡 Suggested Follow-ups:")
#     st.button("Can you explain further?")
#     st.button("Give an example")
#     st.button("What are the real-world uses?")

# # Other utilities
# st.markdown("---")
# st.subheader("💡 AI Assistant Tools")

# for idx, msg in enumerate(st.session_state.chat_history[::-1]):
#     user_text = msg['user']
#     bot_text = msg['bot']

#     # Create a horizontal layout
#     with st.container():
#         cols = st.columns([12, 1])
#         with cols[0]:
#             st.markdown(f"**{idx+1}. You**: {user_text}")
#             st.markdown(f"**🤖 Bot**:")
#             st.code(bot_text, language='markdown')
#         with cols[1]:
#             st.download_button(
#                 label="📥",
#                 data=bot_text,
#                 file_name=f"bot_response_{idx+1}.txt",
#                 key=f"copy_btn_{idx}",
#                 help="Download Response"
#             )

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
    st.code(last_response, language='markdown')
    

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
for msg in st.session_state.chat_history[::-1]:
    with st.expander(f"👤 You: {msg['user']}"):
        st.markdown(f"🧠 Bot Response:")
        st.code(msg['bot'], language='markdown')
        st.download_button("📋 Copy Response", data=msg['bot'], file_name="response.txt")














































# import streamlit as st
# import os
# from dotenv import load_dotenv
# from langchain_core.prompts import ChatPromptTemplate
# from langchain_core.output_parsers import StrOutputParser
# from langchain_google_genai import ChatGoogleGenerativeAI

# # Load environment variables
# load_dotenv()
# GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# # Setup LLM (Gemini)
# llm = ChatGoogleGenerativeAI(
#     model="gemini-2.0-flash",
#     google_api_key=GOOGLE_API_KEY
# )

# prompt_template = ChatPromptTemplate.from_messages([
#     ("system", "You are a helpful, intelligent chatbot."),
#     ("human", "Question: {question}")
# ])

# output_parser = StrOutputParser()
# chain = prompt_template | llm | output_parser

# # Streamlit app UI
# st.set_page_config(page_title="Smart Chatbot Hub", layout="centered")

# # Title
# st.markdown("""
#     <h1 style='text-align: center;'>🤖 Smart Chatbot Hub</h1>
# """, unsafe_allow_html=True)

# # Toolbar buttons that open new tools in new tabs
# col1, col2, col3, col4 = st.columns(4)

# with col1:
#     st.markdown("""<a href="http://localhost:8501/summarizer" target="_blank"><button style='width:100%'>📝 Summarizer Tool</button></a>""", unsafe_allow_html=True)

# with col2:
#     st.markdown("""<a href="http://localhost:8501/grammar" target="_blank"><button style='width:100%'>🧹 Grammar Checker</button></a>""", unsafe_allow_html=True)

# with col3:
#     st.markdown("""<a href="http://localhost:8501/facts" target="_blank"><button style='width:100%'>📚 Random Fact Gen</button></a>""", unsafe_allow_html=True)

# with col4:
#     st.markdown("""<a href="http://localhost:8501/quiz" target="_blank"><button style='width:100%'>🎲 Quiz Generator</button></a>""", unsafe_allow_html=True)

# # Chatbot Mode
# st.subheader("🎛️ Choose Chatbot Mode")
# chatbot_mode = st.selectbox("", ["Default", "Math Expert", "Language Helper", "General Knowledge Bot"])

# # Input Section
# st.subheader("💬 Enter Your Question")
# user_input = st.text_area("", placeholder="Type your question here...", height=100)

# # Ask/Run Button
# if st.button("🧠 Ask/Run"):
#     if user_input:
#         # Enhance prompt based on chatbot mode
#         full_question = f"Mode: {chatbot_mode}. Question: {user_input}"
#         bot_response = chain.invoke({"question": full_question})

#         # Show response
#         st.markdown("---")
#         st.subheader("🤖 Answer")
#         st.info(bot_response)

#         # Allow response to be copied
#         st.download_button(
#             "📋 Download Response",
#             data=bot_response,
#             file_name="response.txt",
#             key=f"download_response_{hash(user_input)}"  # Avoid DuplicateElementId
#         )

# # Chat History Placeholder
# st.markdown("---")
# st.subheader("🕒 Chat History")
# st.caption("(Coming soon: persistent memory and chat logs.)")



