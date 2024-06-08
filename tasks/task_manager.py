import datetime
import pickle
import os

class TaskManager:
    """
    A class to manage tasks in a to-do list, including adding, updating, deleting, and sorting tasks.
    
    Attributes:
        filename (str): The name of the file where tasks are saved.
        tasks (list): The list of tasks.
    """

    def __init__(self, filename="tasks.pkl"):
        """
        Initializes a new TaskManager instance and loads tasks from a file.

        Args:
            filename (str, optional): The name of the file where tasks are saved. Defaults to "tasks.pkl".
        """
        self.filename = filename
        self.tasks = self.load_tasks()

    def add_task(self, task):
        """
        Adds a new task to the task list and saves the updated list to the file.

        Args:
            task (Task): The task to be added.
        """
        self.tasks.append(task)
        self.save_tasks()

    def update_task(self, task_index, **kwargs):
        """
        Updates the attributes of a task and saves the updated list to the file.

        Args:
            task_index (int): The index of the task to be updated.
            **kwargs: The task attributes to be updated.
        """
        for key, value in kwargs.items():
            setattr(self.tasks[task_index], key, value)
        self.save_tasks()

    def delete_task(self, task_index):
        """
        Deletes a task from the task list and saves the updated list to the file.

        Args:
            task_index (int): The index of the task to be deleted.
        """
        self.tasks.pop(task_index)
        self.save_tasks()

    def sort_tasks(self, by="priority"):
        """
        Sorts tasks based on a specified attribute and saves the sorted list to the file.

        Args:
            by (str, optional): The attribute to sort tasks by. Can be "priority", "due date", or "creation date". Defaults to "priority".
        """
        if by == "priority":
            self.tasks.sort(key=lambda task: task.priority)
        elif by == "due date":
            self.tasks.sort(key=lambda task: task.due_date if task.due_date else datetime.max)
        elif by == "creation date":
            self.tasks.sort(key=lambda task: task.creation_date)
        self.save_tasks()

    def save_tasks(self):
        """
        Saves the current list of tasks to a file.
        """
        with open(self.filename, "wb") as file:
            pickle.dump(self.tasks, file)

    def load_tasks(self):
        """
        Loads tasks from a file if it exists, otherwise returns an empty list.

        Returns:
            list: The list of tasks.
        """
        if os.path.exists(self.filename):
            with open(self.filename, "rb") as file:
                return pickle.load(file)
        return []

    def __str__(self):
        """
        Returns a string representation of all tasks in the task list.

        Returns:
            str: A formatted string representing the task list.
        """
        return "\n".join(str(task) for task in self.tasks)
