import streamlit as st


def render_metrics(data):

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Products",
        data.get("products", 0)
    )

    col2.metric(
        "Forecasts",
        data.get("forecast", 0)
    )

    col3.metric(
        "Risk",
        data.get("risk", "LOW")
    )