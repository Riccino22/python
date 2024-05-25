import streamlit as st
import manage_csv as mcsv
import dictionary as dct

st.title("Insert a new word")

with st.form(key="new_word_form"):
    new_word = st.text_input("New word")
    btn = st.form_submit_button(label="Save")
    
    if btn:
        if dct.word_exists(new_word):
            mcsv.insert_word(new_word, "description")
            st.success("Word saved")
        else:
            st.error("Word don't exists")
       
