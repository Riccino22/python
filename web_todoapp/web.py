import streamlit as st
import manage_todos as mgt

todos = mgt.get_todos()

def add_todo():
    new_todo = st.session_state["new_todo"]
    mgt.create_todo(new_todo)

st.title("My todo app")


for todo in todos:
    st.checkbox(todo)


st.text_input(label="todo", placeholder="add a todo", key="new_todo", on_change=add_todo)