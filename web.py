import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    this_todo = st.session_state["new_todo"] + "\n"
    todos.append(this_todo)
    functions.write_todos(todos)


st.title("My todo app")
for i, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox == True:
        todos.pop(i)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()
st.text_input(label="Enter a todo", placeholder="Add a new todo",
              on_change=add_todo, key="new_todo")
