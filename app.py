import streamlit as st
from chatbot import get_answer

st.set_page_config(
    page_title="Context-Aware FAQ Chatbot",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 Context-Aware Intelligent FAQ Chatbot")
st.write("Ask any question from the FAQ dataset.")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.text_input("Enter your question:")

if st.button("Ask") and user_input:
    answer = get_answer(user_input)
    st.session_state.chat_history.append(("You", user_input))
    st.session_state.chat_history.append(("Bot", answer))

for sender, message in st.session_state.chat_history:
    st.write(f"**{sender}:** {message}")
