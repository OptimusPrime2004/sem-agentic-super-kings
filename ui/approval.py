import streamlit as st

def approval_screen():

    st.subheader("Human Approval")

    approve = st.button("Approve Purchase Order")
    reject = st.button("Reject Purchase Order")

    if approve:
        st.session_state.approval_status = "Approved"
        st.success("Purchase Order Approved")

    if reject:
        st.session_state.approval_status = "Rejected"
        st.error("Purchase Order Rejected")

    return approve, reject