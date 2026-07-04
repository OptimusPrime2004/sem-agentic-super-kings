import streamlit as st


def render_timeline():

    st.subheader("Workflow Timeline")

    st.success("Forecast Agent ✓")

    st.success("Inventory Agent ✓")

    st.success("Risk Agent ✓")

    approval_status = st.session_state.get("approval_status", "Pending")

    if approval_status == "Approved":
        st.success("Human Approval Completed")
        st.success("Logistics Ready")
    elif approval_status == "Rejected":
        st.error("Purchase Order Rejected")
        st.info("Workflow Ended")
    else:
        st.warning("Human Approval Pending")
        st.info("Logistics Waiting")