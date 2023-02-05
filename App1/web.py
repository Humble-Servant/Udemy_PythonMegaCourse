import streamlit as st
from modules import functions

tasks = functions.get_tasks()

st.title("My Task List")

for task in tasks:
    st.checkbox(task)

st.text_input(label="", placeholder="Enter a task...")
