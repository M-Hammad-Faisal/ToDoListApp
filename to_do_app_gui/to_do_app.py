import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import simpledialog

from tasks.task import Task
from tasks.task_manager import TaskManager

class ToDoApp:
    """
    A GUI-based To-Do List application using Tkinter.
    Allows users to add, update, delete, complete, and sort tasks.
    """
    def __init__(self, root):
        """
        Initialize the ToDoApp with the main Tkinter root window.
        
        :param root: The main Tkinter root window.
        """
        self.task_manager = TaskManager()
        self.root = root
        self.root.title("To-Do List App")
        self.root.geometry("800x500")
        self.root.config(bg="#f0f0f0")

        # Configure the style for the treeview
        self.style = ttk.Style()
        self.style.configure("Treeview", font=("Helvetica", 12), rowheight=25)
        self.style.configure("Treeview.Heading", font=("Helvetica", 14, "bold"))

        # Set up the treeview widget
        self.tree = ttk.Treeview(root, columns=("Title", "Description", "Priority", "Due Date", "Status"), show="headings")
        self.tree.heading("Title", text="Title")
        self.tree.heading("Description", text="Description")
        self.tree.heading("Priority", text="Priority")
        self.tree.heading("Due Date", text="Due Date")
        self.tree.heading("Status", text="Status")

        # Configure the width of each column
        self.tree.column("Title", width=150)
        self.tree.column("Description", width=200)
        self.tree.column("Priority", width=100)
        self.tree.column("Due Date", width=150)
        self.tree.column("Status", width=100)

        self.tree.pack(fill=tk.BOTH, expand=True, pady=20)

        # Load existing tasks
        self.load_tasks()

        # Set up the button frame
        button_frame = tk.Frame(root, bg="#f0f0f0")
        button_frame.pack(pady=20)

        # Add Task button
        self.add_task_button = tk.Button(button_frame, text="Add Task", command=self.add_task, font=("Helvetica", 12), bg="#4CAF50", fg="#ffffff", padx=10, pady=5)
        self.add_task_button.grid(row=0, column=0, padx=10, pady=5)

        # Update Task button
        self.update_task_button = tk.Button(button_frame, text="Update Task", command=self.update_task, font=("Helvetica", 12), bg="#2196F3", fg="#ffffff", padx=10, pady=5)
        self.update_task_button.grid(row=0, column=1, padx=10, pady=5)

        # Delete Task button
        self.delete_task_button = tk.Button(button_frame, text="Delete Task", command=self.delete_task, font=("Helvetica", 12), bg="#F44336", fg="#ffffff", padx=10, pady=5)
        self.delete_task_button.grid(row=0, column=2, padx=10, pady=5)

        # Mark as Complete button
        self.complete_task_button = tk.Button(button_frame, text="Mark as Complete", command=self.complete_task, font=("Helvetica", 12), bg="#FF9800", fg="#ffffff", padx=10, pady=5)
        self.complete_task_button.grid(row=0, column=3, padx=10, pady=5)

        # Sort Tasks button
        self.sort_task_button = tk.Button(button_frame, text="Sort Tasks", command=self.sort_tasks, font=("Helvetica", 12), bg="#9C27B0", fg="#ffffff", padx=10, pady=5)
        self.sort_task_button.grid(row=0, column=4, padx=10, pady=5)

    def load_tasks(self):
        """
        Load tasks from the TaskManager and display them in the treeview.
        """
        for i in self.tree.get_children():
            self.tree.delete(i)
        for task in self.task_manager.tasks:
            self.tree.insert("", tk.END, values=(task.title, task.description, task.priority, task.due_date, task.status))

    def complete_task(self):
        """
        Mark the selected task as complete.
        """
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showerror("Error", "Please select a task to mark as complete.")
            return

        task_index = self.tree.index(selected_item[0])
        self.task_manager.tasks[task_index].mark_complete()
        self.task_manager.save_tasks()
        self.load_tasks()

    def sort_tasks(self):
        """
        Prompt the user to sort tasks by a chosen attribute.
        """
        sort_by = simpledialog.askstring("Sort By", "Sort tasks by ('Priority', 'Due Date', or 'Creation Date')?", parent=self.root)
        if sort_by:
            sort_by = sort_by.lower()
            if sort_by == 'priority':
                self.task_manager.sort_tasks(by="priority")
            elif sort_by == 'due date':
                self.task_manager.sort_tasks(by="due date")
            elif sort_by == 'creation date':
                self.task_manager.sort_tasks(by="creation date")
            else:
                messagebox.showerror("Error", f"Invalid sorting option: {sort_by}")
                return
            self.load_tasks()

    def add_task(self):
        """
        Open a dialog to add a new task.
        """
        self.edit_task_dialog("Add Task", None)

    def update_task(self):
        """
        Open a dialog to update the selected task.
        """
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showerror("Error", "Please select a task to update.")
            return

        task_index = self.tree.index(selected_item[0])
        task = self.task_manager.tasks[task_index]
        self.edit_task_dialog("Update Task", task, task_index)

    def delete_task(self):
        """
        Delete the selected task.
        """
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showerror("Error", "Please select a task to delete.")
            return

        task_index = self.tree.index(selected_item[0])
        self.task_manager.delete_task(task_index)
        self.load_tasks()

    def edit_task_dialog(self, title, task=None, task_index=None):
        """
        Open a dialog to add or update a task.
        
        :param title: The title of the dialog.
        :param task: The task to update (if any).
        :param task_index: The index of the task to update (if any).
        """
        dialog = tk.Toplevel(self.root)
        dialog.title(title)
        dialog.geometry("400x370")
        dialog.config(bg="#f0f0f0")

        # Title entry
        tk.Label(dialog, text="Title:", font=("Helvetica", 12), bg="#f0f0f0").pack(pady=5)
        title_entry = tk.Entry(dialog, font=("Helvetica", 12))
        title_entry.pack(pady=5)
        if task:
            title_entry.insert(0, task.title)

        # Description entry
        tk.Label(dialog, text="Description:", font=("Helvetica", 12), bg="#f0f0f0").pack(pady=5)
        description_entry = tk.Entry(dialog, font=("Helvetica", 12))
        description_entry.pack(pady=5)
        if task:
            description_entry.insert(0, task.description)

        # Priority entry
        tk.Label(dialog, text="Priority:", font=("Helvetica", 12), bg="#f0f0f0").pack(pady=5)
        priority_entry = tk.Entry(dialog, font=("Helvetica", 12))
        priority_entry.pack(pady=5)
        if task:
            priority_entry.insert(0, task.priority)

        # Due date entry
        tk.Label(dialog, text="Due Date:", font=("Helvetica", 12), bg="#f0f0f0").pack(pady=5)
        due_date_entry = tk.Entry(dialog, font=("Helvetica", 12))
        due_date_entry.pack(pady=5)
        if task and task.due_date:
            due_date_entry.insert(0, task.due_date)

        def save_task():
            """
            Save the task from the dialog input fields.
            """
            title = title_entry.get()
            description = description_entry.get()
            priority = int(priority_entry.get())
            due_date = due_date_entry.get()

            if not title:
                messagebox.showerror("Error", "Title is required.")
                return

            if task:
                self.task_manager.update_task(task_index, title=title, description=description, priority=priority, due_date=due_date)
            else:
                new_task = Task(title, description, priority, due_date)
                self.task_manager.add_task(new_task)

            dialog.destroy()
            self.load_tasks()

        # Save button
        save_button = tk.Button(dialog, text="Save", command=save_task, font=("Helvetica", 12), bg="#4CAF50", fg="#ffffff")
        save_button.pack(pady=20)

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
