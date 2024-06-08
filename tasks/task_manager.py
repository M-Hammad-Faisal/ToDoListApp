import datetime
import pickle
import os
from .task import Task

class TaskManager:
    def __init__(self, filename="tasks.pkl"):
        self.filename = filename
        self.tasks = self.load_tasks()

    def add_task(self, task):
        self.tasks.append(task)
        self.save_tasks()

    def update_task(self, task_index, **kwargs):
        for key, value in kwargs.items():
            setattr(self.tasks[task_index], key, value)
        self.save_tasks()

    def delete_task(self, task_index):
        self.tasks.pop(task_index)
        self.save_tasks()

    def sort_tasks(self, by="priority"):
        if by == "priority":
            self.tasks.sort(key=lambda task: task.priority)
        elif by == "due date":
            self.tasks.sort(key=lambda task: task.due_date if task.due_date else datetime.max)
        elif by == "creation date":
            self.tasks.sort(key=lambda task: task.creation_date)
        self.save_tasks()

    def save_tasks(self):
        with open(self.filename, "wb") as file:
            pickle.dump(self.tasks, file)

    def load_tasks(self):
        if os.path.exists(self.filename):
            with open(self.filename, "rb") as file:
                return pickle.load(file)
        return []

    def __str__(self):
        return "\n".join(str(task) for task in self.tasks)
