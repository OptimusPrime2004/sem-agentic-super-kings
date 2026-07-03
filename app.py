import streamlit as st

from graph.graph_builder import graph

from ui.dashboard import render_dashboard
from ui.sidebar import render_sidebar
from ui.chat import render_chat
from ui.timeline import render_timeline
from ui.logs import render_logs
from ui.approval import approval_screen


st.set_page_config(
    page_title="HexaFlow AI",
    page_icon="🚚",
    layout="wide"
)

# ------------------------
# Session State
# ------------------------

if "logs" not in st.session_state:
    st.session_state.logs = []

if "approval_status" not in st.session_state:
    st.session_state.approval_status = "Pending"

if "response" not in st.session_state:
    st.session_state.response = ""

# ------------------------
# Sidebar
# ------------------------

page = render_sidebar()

# ------------------------
# Dashboard
# ------------------------

if page == "Dashboard":

    render_dashboard()

    question = render_chat()

    if question:

        state = {

            "user_query": question,

            "inventory": {},

            "forecast": {},

            "procurement": {},

            "risk": {},

            "logistics": {},

            "communication": {},

            "approval_status":

                st.session_state.approval_status,

            "logs": [],

            "final_response": ""

        }

        result = graph.invoke(state)

        st.session_state.logs = result["logs"]

        st.session_state.response = result

        st.success("Workflow Completed")

# ------------------------
# AI Copilot
# ------------------------

elif page == "AI Copilot":

    st.title("🤖 Supply Chain Copilot")

    query = st.chat_input("Ask a question...")

    if query:

        state = {

            "user_query": query,

            "inventory": {},

            "forecast": {},

            "procurement": {},

            "risk": {},

            "logistics": {},

            "communication": {},

            "approval_status":

                st.session_state.approval_status,

            "logs": [],

            "final_response": ""

        }

        result = graph.invoke(state)

        st.write(result)

# ------------------------
# Workflow
# ------------------------

elif page == "Workflow":

    st.title("Workflow Timeline")

    render_timeline()

# ------------------------
# Approval
# ------------------------

elif page == "Approval":

    approve, reject = approval_screen()

    if approve:

        st.session_state.approval_status = "Approved"

        st.success("Purchase Order Approved")

    if reject:

        st.session_state.approval_status = "Rejected"

        st.error("Purchase Order Rejected")

# ------------------------
# Analytics
# ------------------------

elif page == "Analytics":

    st.title("Analytics Dashboard")

    st.metric(
        "Inventory Health",
        "92%"
    )

    st.metric(
        "Supplier Risk",
        "Medium"
    )

    st.metric(
        "Forecast Accuracy",
        "89%"
    )

# ------------------------
# Logs
# ------------------------

elif page == "Logs":

    render_logs(

        st.session_state.logs

    )