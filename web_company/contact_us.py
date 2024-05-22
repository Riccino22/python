import streamlit as st
import send_email as sem
st.header("Contact Us")

with st.form(key="email_forms"):
    user_email = st.text_input("Your email address")
    category = st.selectbox("Select a category", ["Social", "Professional", "Other"])
    message = st.text_area("Your message")
    btn_send = st.form_submit_button()
    if btn_send:
        sem.send(user_email, category, message)
        