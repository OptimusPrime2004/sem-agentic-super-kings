import streamlit as st


def render_chat():

    st.subheader("🤖 AI Supply Chain Copilot")

    question = st.chat_input(
        "Ask anything..."
    )

    return question