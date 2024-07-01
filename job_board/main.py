import streamlit as st
import manage_json as mjson
import manage_csv as mcsv

st.title("Find Job")
with st.form(key="email_forms"):
    name = st.text_input("Full name")
    email = st.text_input("Email")
    phone = st.text_input("Phone")
    tags = st.multiselect("Tags", mcsv.get_tags())
    btn = st.form_submit_button()
    if btn:
        mjson.add_to_json("seekers.json", {
            "name": name,
            "email": email,
            "phone": phone,
            "tags": tags
        })
