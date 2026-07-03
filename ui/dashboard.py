import streamlit as st


def render_dashboard():

    st.title("🚚 HexaFlow AI")

    st.subheader("Enterprise Supply Chain Control Tower")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Inventory Health", "92%")

    col2.metric("Low Stock", "4")

    col3.metric("Purchase Orders", "7")

    col4.metric("Delayed Shipments", "2")

    st.divider()