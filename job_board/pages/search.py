import streamlit as st
import manage_csv as mcsv
st.set_page_config(layout="wide")
st.title("Search Offer By Tags")
with st.form(key="search"):
    col1, col2 = st.columns([4,1])
    
    with col1:
        tags = st.multiselect("Tags", mcsv.get_tags())
    with col2:
        st.write("")
        st.write("")
        btn = st.form_submit_button("Search")
    
    if btn:
        st.experimental_rerun()
    
for tag in tags:
    st.write(f"## {tag}")