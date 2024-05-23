import streamlit as st

st.title("Get your ticket for the best event")
with st.form(key="email_forms"):
    name = st.text_input(label="Your full name")
    email = st.text_input(label="Your email")
    quantity = st.number_input(label="ticket quantity")
    btn = st.form_submit_button()

    if btn:
        print("get")