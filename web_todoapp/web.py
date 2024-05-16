import streamlit as st
import manage_todos as mgt

todos = mgt.get_todos()

def add_todo():
    new_todo = st.session_state["new_todo"]
    mgt.create_todo(new_todo)

st.title("My todo app")


for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=f"todo_{index}")
    print(checkbox)
    if checkbox:
        print(checkbox)
        mgt.delete_todo(index)
        st.experimental_rerun()


st.text_input(label="todo", placeholder="add a todo", key="new_todo", on_change=add_todo)

st.session_state