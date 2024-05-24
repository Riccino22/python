import streamlit as st
import manage_json as mjson
import manage_csv as mcsv
st.title("Find Job")
with st.form(key="email_forms"):
    name = st.text_input("Full name")
    email = st.text_input("Email")
    phone = st.text_input("Phone")
    tags = st.multiselect("Sle", mcsv.get_tags())
    btn = st.form_submit_button()
    if btn:
        mjson.add_seeker(name, email, phone, tags)