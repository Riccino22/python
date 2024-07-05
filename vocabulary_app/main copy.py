import streamlit as st
import manage_json as mjson
import dictionary as dct
import time

print("New user")
st.title("Insert a new word")

# Function to save a new word
def save_word(new_word):
    with st.spinner('Loading...'):
        exists, definition = dct.word_exists(new_word)
        if exists:
            mjson.insert_word(new_word, dct.translate_word(new_word), definition)
        print(exists)
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


words = mjson.get_words()
words.reverse()
for index, word in enumerate(words):
    col1, col2 = st.columns(2)
    with col1:
        st.write(f"<p style='font-size: 30px;'>{word['word']}</p>", unsafe_allow_html=True)
    with col2:
        st.write(f"<p style='font-size: 30px;'>{word['translation']}</p>", unsafe_allow_html=True)
        
    col3, col4 = st.columns([6,1])

    with col3:
        with st.expander("Definition"):
            st.write(word["definitions"])
    with col4:
        st.button("Delete", key="delete_btn_" + str(index))
        if st.session_state["delete_btn_" + str(index)]:
            mjson.delete_word(index)
            st.experimental_rerun()
    
