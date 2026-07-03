import streamlit as st


def render_timeline():

    st.subheader("Workflow Timeline")

    st.success("Forecast Agent ✓")

    st.success("Inventory Agent ✓")

    st.success("Risk Agent ✓")

    st.warning("Human Approval Pending")

    st.info("Logistics Waiting")