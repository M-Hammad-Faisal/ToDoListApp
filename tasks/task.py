from datetime import datetime

class Task:
    """
    A class to represent a task in the to-do list.

    Attributes:
        title (str): The title of the task.
        description (str): The description of the task.
        priority (int): The priority level of the task.
        due_date (datetime): The due date for the task.
        creation_date (datetime): The date and time when the task was created.
        is_complete (bool): The completion status of the task.
    """

    def __init__(self, title, description=None, priority=0, due_date=None):
        """
        Initializes a new Task instance.

        Args:
            title (str): The title of the task.
            description (str, optional): The description of the task. Defaults to None.
            priority (int, optional): The priority level of the task. Defaults to 0.
            due_date (datetime, optional): The due date for the task. Defaults to None.
        """
        self.title = title
        self.description = description
        self.priority = priority
        self.due_date = due_date
        self.creation_date = datetime.now()
        self.is_complete = False

    def mark_complete(self):
        """
        Marks the task as complete.
        """
        self.is_complete = True

    @property
    def status(self):
        """
        Returns the completion status of the task as a string.

        Returns:
            str: "Complete" if the task is complete, otherwise "Incomplete".
        """
        return "Complete" if self.is_complete else "Incomplete"

    def __str__(self):
        """
        Returns a string representation of the task.

        Returns:
            str: A formatted string describing the task.
        """
        return f"""
    Title: {self.title}
    Description: {self.description}
    Priority: {self.priority}
    Due Date: {self.due_date}
    Creation Date: {self.creation_date}
    Complete: {self.is_complete}
    """
