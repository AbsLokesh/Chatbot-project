import streamlit as st
from utils.llm_client import anthropic_chat
from utils.memory import init_session, add_message

st.set_page_config(page_title="Chatbot", page_icon="🤖", layout="centered")

# Initialize memory
init_session()

st.title("🤖 My AI Chatbot")

# Display conversation
for msg in st.session_state["messages"]:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# User input
if prompt := st.chat_input("Type your message..."):
    add_message("user", prompt)
    with st.chat_message("user"):
        st.write(prompt)

    # Get response
    with st.chat_message("assistant"):
        response = anthropic_chat(st.session_state["messages"])
        st.write(response)

    add_message("assistant", response)
