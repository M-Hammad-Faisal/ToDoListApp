import argparse
from tasks.task import Task
from tasks.task_manager import TaskManager

def main():
    parser = argparse.ArgumentParser(description="To-Do List App")
    subparsers = parser.add_subparsers(dest="command")

    subparsers.add_parser("view", help="View all current tasks")

    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("title", help="Title of the task")
    add_parser.add_argument("--description", help="Description of the task", default="")
    add_parser.add_argument("--priority", type=int, help="Priority of the task", default=0)
    add_parser.add_argument("--due_date", help="Due date of the task", default=None)

    update_parser = subparsers.add_parser("update", help="Update an existing task")
    update_parser.add_argument("index", type=int, help="Index of the task to update")
    update_parser.add_argument("--title", help="New title of the task")
    update_parser.add_argument("--description", help="New description of the task")
    update_parser.add_argument("--priority", type=int, help="New priority of the task")
    update_parser.add_argument("--due_date", help="New due date of the task")

    subparsers.add_parser("delete", help="Delete a task").add_argument("index", type=int, help="Index of the task to delete")
    subparsers.add_parser("complete", help="Mark a task as complete").add_argument("index", type=int, help="Index of the task to mark as complete")
    subparsers.add_parser("sort", help="Sort tasks").add_argument("by", choices=["priority", "due_date", "creation_date"], help="Sort tasks by this field")

    args = parser.parse_args()
    task_manager = TaskManager()

    if args.command == "view":
        print(task_manager)
    elif args.command == "add":
        new_task = Task(args.title, args.description, args.priority, args.due_date)
        task_manager.add_task(new_task)
    elif args.command == "update":
        update_fields = {k: v for k, v in vars(args).items() if k != "command" and k != "index" and v is not None}
        task_manager.update_task(args.index, **update_fields)
    elif args.command == "delete":
        task_manager.delete_task(args.index)
    elif args.command == "complete":
        task_manager.tasks[args.index].mark_complete()
        task_manager.save_tasks()
    elif args.command == "sort":
        task_manager.sort_tasks(by=args.by)

if __name__ == "__main__":
    main()
