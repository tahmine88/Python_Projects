import tkinter as tk
from tkinter import messagebox

class ToDoListApp:
    def __init__(self, master):
        self.master = master
        self.master.title("To-Do List")

        # Label for the entry box
        self.label = tk.Label(master, text="Enter a new task:", font=("Helvetica", 14))
        self.label.pack(pady=10)

        # Entry box for adding new tasks
        self.entry = tk.Entry(master, width=40)
        self.entry.pack(pady=10)

        # Add Task Button
        self.add_button = tk.Button(master, text="Add Task", command=self.add_task, font=("Helvetica", 12), bg="green", fg="white")
        self.add_button.pack(pady=5)

        # Listbox to display tasks
        self.listbox = tk.Listbox(master, width=50, height=10)
        self.listbox.pack(pady=10)

        # Complete Task Button
        self.complete_button = tk.Button(master, text="Complete Task", command=self.complete_task, font=("Helvetica", 12), bg="blue", fg="white")
        self.complete_button.pack(pady=5)

        # Remove Task Button
        self.remove_button = tk.Button(master, text="Remove Task", command=self.remove_task, font=("Helvetica", 12), bg="red", fg="white")
        self.remove_button.pack(pady=5)

    def add_task(self):
        task = self.entry.get()
        if task != "":
            self.listbox.insert(tk.END, task)
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Please enter a task.")

    def complete_task(self):
        try:
            selected_task_index = self.listbox.curselection()[0]
            task = self.listbox.get(selected_task_index)
            self.listbox.delete(selected_task_index)
            self.listbox.insert(tk.END, f"{task} - Completed")
        except:
            messagebox.showwarning("Selection Error", "Please select a task to complete.")

    def remove_task(self):
        try:
            selected_task_index = self.listbox.curselection()[0]
            self.listbox.delete(selected_task_index)
        except:
            messagebox.showwarning("Selection Error", "Please select a task to remove.")

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()
