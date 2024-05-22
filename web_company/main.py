import streamlit as st
import read_csv as rcsv
import pandas as ps


members = rcsv.read_members_file()

st.set_page_config(layout="wide")
st.title("The Best Company")
st.write("This is the best company")
counter = 0
col1, col2, col3 = st.columns(3)

def memberLayout(col, member):
    with col:
        st.header(f"{member['first name']}  {member['last name']}")
        st.write(member["role"])
        st.image("static/" + member["image"], width=200)
        
for member in members:
    counter += 1
    if counter == 1:
        memberLayout(col1, member)
    elif counter == 2:
        memberLayout(col2, member)
    else:
        memberLayout(col3, member)
        counter = 0
        