import streamlit as st
import manage_csv as mcsv
import dictionary as dct
import time

st.title("Insert a new word")

# Function to save a new word
def save_word(new_word):
    with st.spinner('Loading...'):
        exists, definition = dct.word_exists(new_word)
        if exists:
            print(exists)
            mcsv.insert_word(new_word, dct.translate_word(new_word), definition)
    return exists

# User interface
with st.form(key="new_word_form"):
    new_word = st.text_input("New word")
    btn = st.form_submit_button(label="Save")

    if btn:
        exists = save_word(new_word)
        if exists:
            st.success("Word saved successfully") 
        else:
            st.error("The word does not exist")
