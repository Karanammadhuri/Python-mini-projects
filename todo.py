import tkinter as tk

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)

def delete_task():
    try:
        index = listbox.curselection()[0]
        listbox.delete(index)
    except IndexError:
        pass

# Create the main window
root = tk.Tk()
root.title("To-Do List")

# Create a listbox to display tasks
listbox = tk.Listbox(root, width=500)
listbox.pack(pady=10)

# Create an entry widget for adding tasks
entry = tk.Entry(root, width=500)
entry.pack(pady=10)

# Create buttons for adding and deleting tasks
add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack(side=tk.LEFT, padx=50)
delete_button = tk.Button(root, text="Delete Task", command=delete_task)
delete_button.pack(side=tk.TOP, padx=50)

# Run the application
root.mainloop()
