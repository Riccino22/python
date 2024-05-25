import streamlit as st

st.title("Insert a new word")

with st.form(key="new_word_form"):
    new_word = st.text_input("New word")
    btn = st.form_submit_button(label="Save")