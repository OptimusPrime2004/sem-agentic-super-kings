import streamlit as st


def render_sidebar():

    with st.sidebar:

        st.title("HexaFlow AI")

        page = st.radio(

            "Navigation",

            [

                "Dashboard",

                "AI Copilot",

                "Workflow",

                "Approval",

                "Analytics",

                "Logs"

            ]

        )

    return page