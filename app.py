from dotenv import load_dotenv
load_dotenv()

import streamlit as st

from graph.graph_builder import graph

from ui.dashboard import render_dashboard
from ui.sidebar import render_sidebar
from ui.chat import render_chat
from ui.timeline import render_timeline
from ui.logs import render_logs
from ui.approval import approval_screen


def render_workflow_result(result):

    if result.get("final_response"):
        st.markdown(result["final_response"])
        return

    inventory = result.get("inventory", {})
    if inventory.get("low_stock_items"):
        st.markdown("### Low Stock Items")
        st.write(
            f"Low stock items: {inventory.get('low_stock_count', len(inventory['low_stock_items']))}"
        )
        st.table(inventory["low_stock_items"])

    forecast = result.get("forecast", {})
    if forecast.get("high_demand_products"):
        st.markdown("### High Demand Products")
        st.table(forecast["high_demand_products"][:10])

    procurement = result.get("procurement", {})
    if procurement.get("output"):
        st.markdown("### Procurement Response")
        st.text(procurement["output"])

    risk = result.get("risk", {})
    if risk.get("output"):
        st.markdown("### Risk Response")
        st.text(risk["output"])

    if not any([
        inventory.get("low_stock_items"),
        forecast.get("high_demand_products"),
        procurement.get("output"),
        risk.get("output")
    ]):
        st.json(result)


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

if "workflow_state" not in st.session_state:
    st.session_state.workflow_state = None

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

            "approval_status": st.session_state.approval_status,

            "logs": [],

            "final_response": ""

        }

        # Save workflow state
        st.session_state.workflow_state = state

        result = graph.invoke(state)

        # Update workflow state
        st.session_state.workflow_state = result

        st.session_state.logs = result["logs"]

        st.session_state.response = result

        render_workflow_result(result)

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

            "approval_status": st.session_state.approval_status,

            "logs": [],

            "final_response": ""

        }

        # Save workflow state
        st.session_state.workflow_state = state

        result = graph.invoke(state)

        # Update workflow state
        st.session_state.workflow_state = result
        render_workflow_result(result)

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

        if st.session_state.workflow_state is not None:

            st.session_state.workflow_state["approval_status"] = "Approved"

            result = graph.invoke(st.session_state.workflow_state)

            st.session_state.workflow_state = result

            st.session_state.logs = result["logs"]

            st.session_state.response = result

        st.success("Purchase Order Approved")

    if reject:

        st.session_state.approval_status = "Rejected"

        if st.session_state.workflow_state is not None:

            st.session_state.workflow_state["approval_status"] = "Rejected"

            result = graph.invoke(st.session_state.workflow_state)

            st.session_state.workflow_state = result

            st.session_state.logs = result["logs"]

            st.session_state.response = result

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