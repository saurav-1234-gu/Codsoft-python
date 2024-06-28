import tkinter as tk
from tkinter import messagebox

class TodoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")

        
        self.tasks = []

        
        self.task_entry = tk.Entry(root, width=30)
        self.task_entry.grid(row=0, column=0, padx=5, pady=5)

        self.add_button = tk.Button(root, text="Add", command=self.add_task)
        self.add_button.grid(row=0, column=1, padx=5, pady=5)

        self.delete_button = tk.Button(root, text="Delete", command=self.delete_task)
        self.delete_button.grid(row=1, column=0, padx=5, pady=5)

        self.update_button = tk.Button(root, text="Update", command=self.update_task)
        self.update_button.grid(row=1, column=1, padx=5, pady=5)

        self.view_button = tk.Button(root, text="View", command=self.view_tasks)
        self.view_button.grid(row=2, column=0, padx=5, pady=5)

        self.quit_button = tk.Button(root, text="Quit", command=root.quit)
        self.quit_button.grid(row=2, column=1, padx=5, pady=5)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            messagebox.showinfo("Task Added", f"Task '{task}' added successfully.")
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Empty Task", "Please enter a task.")

    def delete_task(self):
        selected_task = self.task_entry.get()
        if selected_task in self.tasks:
            self.tasks.remove(selected_task)
            messagebox.showinfo("Task Deleted", f"Task '{selected_task}' deleted successfully.")
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Task Not Found", f"Task '{selected_task}' not found.")

    def update_task(self):
        selected_task = self.task_entry.get()
        if selected_task in self.tasks:
            new_task = simpledialog.askstring("Update Task", f"Update '{selected_task}' to:")
            if new_task:
                self.tasks[self.tasks.index(selected_task)] = new_task
                messagebox.showinfo("Task Updated", f"Task '{selected_task}' updated to '{new_task}'.")
        else:
            messagebox.showwarning("Task Not Found", f"Task '{selected_task}' not found.")
        self.task_entry.delete(0, tk.END)

    def view_tasks(self):
        if self.tasks:
            messagebox.showinfo("Tasks", "\n".join(self.tasks))
        else:
            messagebox.showinfo("Empty List", "No tasks to display.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoListApp(root)
    root.mainloop()
















# import tkinter as tk
# from tkinter import messagebox

# class ToDoList:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("To-Do List")
#         self.tasks = []

#         self.task_list = tk.Listbox(self.root, width=40)
#         self.task_list.pack(padx=10, pady=10)

#         self.entry = tk.Entry(self.root, width=40)
#         self.entry.pack(padx=10, pady=10)

#         self.add_button = tk.Button(self.root, text="Add", command=self.add_task)
#         self.add_button.pack(padx=10, pady=10)

#         self.view_button = tk.Button(self.root, text="View", command=self.view_tasks)
#         self.view_button.pack(padx=10, pady=10)

#         self.update_button = tk.Button(self.root, text="Update", command=self.update_task)
#         self.update_button.pack(padx=10, pady=10)

#         self.delete_button = tk.Button(self.root, text="Delete", command=self.delete_task)
#         self.delete_button.pack(padx=10, pady=10)

#         self.quit_button = tk.Button(self.root, text="Quit", command=self.root.quit)
#         self.quit_button.pack(padx=10, pady=10)

#     def add_task(self):
#         task = self.entry.get()
#         if task:
#             self.tasks.append(task)
#             self.task_list.insert(tk.END, task)
#             self.entry.delete(0, tk.END)

#     def view_tasks(self):
#         self.task_list.delete(0, tk.END)
#         for task in self.tasks:
#             self.task_list.insert(tk.END, task)

#     def update
