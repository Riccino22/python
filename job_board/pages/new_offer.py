import streamlit as st
import manage_csv as mcsv
import manage_json as mjson
import send_email
st.title("Publish New Offer")
with st.form(key="offer_form"):
    title = st.text_input("Title", key="title")
    tags = st.multiselect("Tags", mcsv.get_tags())
    btn = st.form_submit_button()
    
    if btn:
        mjson.add_to_json("offers.json", {
            "title": title,
            "tags": tags
        })        
        send_email.send(tags, title)
        st.success("Offer published successfully")