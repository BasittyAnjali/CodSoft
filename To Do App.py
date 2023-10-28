import tkinter as tk
from tkinter import messagebox

def add_task():
    title = task_entry.get()
    if title:
        task_list.insert(tk.END, title)
        task_entry.delete(0, tk.END)
        messagebox.showinfo("Success", f"Task '{title}' added successfully.")
    else:
        messagebox.showwarning("Warning", "Please enter a task!")

def update_task():
    selected_task = task_list.curselection()
    if selected_task:
        index = selected_task[0]
        updated_title = task_entry.get()
        if updated_title:
            task_list.delete(index)
            task_list.insert(index, updated_title)
            task_entry.delete(0, tk.END)
            messagebox.showinfo("Success", f"Task updated successfully.")
        else:
            messagebox.showwarning("Warning", "Please enter an updated task!")
    else:
        messagebox.showwarning("Warning", "Please select a task to upload!")

def mark_done():
    selected_task = task_list.curselection()
    if selected_task:
        index = selected_task[0]
        task_list.itemconfig(index, {'bg': 'light green'})
        task_entry.delete(0, tk.END)
        task_title = task_list.get(index)
        messagebox.showinfo("Success", f"Task '{task_title}' marked as done.")
    else:
        messagebox.showwarning("Warning", "Please select a task to mark as done!")

app = tk.Tk()
app.title("To-Do List")

header_label = tk.Label(app, text="To-Do List Application", font=("Arial", 20))
header_label.pack(pady=10)  # Add padding to the top of the header label

task_label = tk.Label(app, text="Enter Task:")
task_label.pack(pady=5)

task_entry = tk.Entry(app)
task_entry.pack(pady=10)

add_button = tk.Button(app, text="Add Task", command=add_task)
add_button.pack(pady=5)

update_button = tk.Button(app, text="Update Task", command=update_task)
update_button.pack(pady=5)

mark_done_button = tk.Button(app, text="Mark as Done", command=mark_done)
mark_done_button.pack(pady=5)

task_list = tk.Listbox(app)
task_list.pack()

app.mainloop()
