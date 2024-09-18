import streamlit as st

if 'tote' not in st.session_state:
    st.session_state.tote = 0.0

st.title("Order total and history")
amount = st.number_input("Enter an Amount")
total = st.button("Total")
clear = st.button("Clear")

if total:
    st.session_state.tote += amount
    amount = 0.0
    st.write(f"The total is {st.session_state.tote}.")

if clear:
    st.session_state.tote = 0.0
    amount = None
    st.rerun()
