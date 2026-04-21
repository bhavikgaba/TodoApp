import streamlit as st
import json
import os
FILE_NAME = "tasks.json"
def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []
    with open("tasks.json", 'r') as f:
        try:
            return json.load(f)
        except:
            return []
def save_tasks(tasks):
    with open("tasks.json", "w") as f:
        json.dump(tasks, f, indent = 4)
st.title("TODO App")
tasks = load_tasks()
st.subheader("Add Tasks")
new_task = st.text_input("Enter task")
if st.button("Add"):
    if new_task:
        tasks.append({"title" : new_task, "done" : False})
        save_tasks(tasks)
        st.success("Task added!")
    else:
        st.warning("Enter a task")
st.subheader("Your Tasks")
if not tasks:
    st.write("No tasks available")
else:
    for i, task in enumerate(tasks):
        col1, col2, col3 = st.columns([5, 1, 1])
        status = "✔" if task["done"] else "✘"
        col1.write(f"{i + 1}. [{status}] {task['title']}")
        if col2.button("Done", key = f"done_{i}"):
            tasks[i]["done"] = True
            save_tasks(tasks)
            st.rerun()
        if col3.button("Delete", key = f"del_{i}"):
            tasks.pop(i)
            save_tasks(tasks)
            st.rerun()