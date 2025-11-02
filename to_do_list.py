
import tkinter as tkr

root = tkr.Tk()
root.title("My To-Do List")
root.geometry("350x400")
root.config(bg="#FDF6EC")

tasks = []

def add():
    task = task_entry.get().strip()
    if task:
        tasks.append(task)
        update_list()
        task_entry.delete(0, tkr.END)

def delete():
    selected = task_listbox.curselection()
    if selected:
        index = selected[0]
        tasks.pop(index)
        update_list()

def clear():
    tasks.clear()
    update_list()

def update_list():
    task_listbox.delete(0, tkr.END)
    for i, task in enumerate(tasks, start=1):
        task_listbox.insert(tkr.END, f"{i}. {task}")

tkr.Label(root, text="To-Do List", font=("Arial", 16, "bold"), bg="#FDF6EC", fg="#333").pack(pady=10)

task_entry = tkr.Entry(root, font=("Arial", 12), width=25)
task_entry.pack(pady=5)

add_btn = tkr.Button(root, text="Add Task", command=add, bg="#90EE90", width=12)
add_btn.pack(pady=3)

delete_btn = tkr.Button(root, text="Delete Task", command=delete, bg="#FF7F7F", width=12)
delete_btn.pack(pady=3)

clear_btn = tkr.Button(root, text="Clear All", command=clear, bg="#FFD580", width=12)
clear_btn.pack(pady=3)

task_listbox = tkr.Listbox(root, width=40, height=12, font=("Arial", 11))
task_listbox.pack(pady=10)

root.mainloop()
