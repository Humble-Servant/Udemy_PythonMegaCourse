import streamlit as st
from modules import functions

tasks = functions.get_tasks()


def add_task():
    task = st.session_state["new_task"] + "\n"
    tasks.append(task)
    functions.write_tasks(tasks)


st.title("My Task List")

for task in tasks:
    st.checkbox(task)

st.text_input(label=" ", placeholder="Enter a task...", on_change=add_task, key="new_task")

st.session_state
