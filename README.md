# To-Do List Application
This is a To-Do List application built with Python, featuring both a command-line interface (CLI) and a graphical user interface (GUI) using Tkinter. Users can add, update, delete, complete, and sort tasks.

## Features
- Add Task: Add a new task with a title, description, priority, and due date.
- Update Task: Update an existing task's details.
- Delete Task: Remove a task from the list.
- Complete Task: Mark a task as complete.
- Sort Tasks: Sort tasks by priority, due date, or creation date.
- View Tasks: View all tasks in a detailed list.

## Requirements
- Python 3.6 or higher
- Tkinter (should be included with Python by default)

## Project Structure
```markdown
ToDoListApp/
├── tasks/
│   ├── __init__.py
│   ├── task.py
│   └── task_manager.py
├── to_do_app_cli/
│   ├── __init__.py
│   └── to_do_app.py
├── to_do_app_gui/
│   ├── __init__.py
│   └── to_do_app.py
└── .gitignore
└── README.md
```

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/M-Hammad-Faisal/to-do-list-app.git
    cd to-do-list-app
    ```
   
2. Create and activate a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

## Usage
### Command-Line Interface (CLI)
The CLI allows you to manage your tasks through terminal commands. Run the `to_do_app.py` script in the `to_do_app_cli` directory with the desired command.

Add a task:
```bash
python to_do_app_cli/to_do_app.py add "Title of Task" --description "Description of the task" --priority 1 --due_date "2024-06-01"
```

Update a task:
```bash
python to_do_app_cli/to_do_app.py update 0 --title "Updated Title" --description "Updated description" --priority 2 --due_date "2024-06-10"
```

Mark a task as complete:
```bash
python to_do_app_cli/to_do_app.py complete 0
```

Sort tasks:
```bash
python to_do_app_cli/to_do_app.py sort priority
```

View tasks:
```bash
python to_do_app_cli/to_do_app.py view
```

Delete a task:
```bash
python to_do_app_cli/to_do_app.py delete 0
```

### Graphical User Interface (GUI)
The GUI provides an interactive way to manage your tasks. Run the `to_do_app.py` script in the `to_do_app_gui` directory to start the application.

```bash
python -m to_do_app_gui/to_do_app.py
```

## GUI Features
1. Add Task: Click "Add Task" and fill in the task details in the pop-up dialog.
2. Update Task: Select a task and click "Update Task" to modify its details.
3. Delete Task: Select a task and click "Delete Task" to remove it.
4. Complete Task: Select a task and click "Mark as Complete" to mark it as done.
5. Sort Tasks: Click "Sort Tasks" and specify the sorting criteria in the pop-up dialog.
6. View Tasks: The main window displays all tasks with their details.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.
