import streamlit as st
import manage_csv as mcsv
import manage_json as mjson

st.set_page_config(layout="wide")
st.title("Search Offer By Tags")

offers = mjson.get_json("offers.json")
with st.form(key="search"):
    col1, col2 = st.columns([4,1])
    
    with col1:
        tags = st.multiselect("Tags", mcsv.get_tags())
    with col2:
        st.write("")
        st.write("")
        btn = st.form_submit_button("Search")
    
    if btn:
        for offer in offers:
            if all([tag in offer["tags"] for tag in tags]):
                with st.container():
                    st.subheader(offer["title"])
                    st.write(offer["description"])
                   
    
        
