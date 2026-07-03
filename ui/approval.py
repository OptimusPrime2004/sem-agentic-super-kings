import streamlit as st


def approval_screen():

    st.subheader("Human Approval")

    approve = st.button(
        "Approve Purchase Order"
    )

    reject = st.button(
        "Reject Purchase Order"
    )

    return approve, reject