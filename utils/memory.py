import streamlit as st

def init_session():
    if "messages" not in st.session_state:
        st.session_state["messages"] = [{"role": "assistant", "content": "Hi, I’m your chatbot 🤖. How can I help you today?"}]

def add_message(role, content):
    st.session_state["messages"].append({"role": role, "content": content})
