import streamlit as st
import manage_csv as mc
st.title("Find Job")
with st.form(key="email_forms"):
    name = st.text_input("Full name")
    email = st.text_input("Email")
    phone = st.text_input("Phone")
    btn = st.form_submit_button()
    if btn:
        mc.add_seeker(name)