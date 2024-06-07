from datetime import datetime


class Task:
    def __init__(self, title, description=None, priority=0, due_date=None):
        self.title = title
        self.description = description
        self.priority = priority
        self.due_date = due_date
        self.creation_date = datetime.now()
        self.is_complete = False

    def mark_complete(self):
        self.is_complete = True

    def __str__(self):
        return f"""
    Title: {self.title}
    Description: {self.description}
    Priority: {self.priority}
    Due Date: {self.due_date}
    Creation Date: {self.creation_date}
    Complete: {self.is_complete}
    """
