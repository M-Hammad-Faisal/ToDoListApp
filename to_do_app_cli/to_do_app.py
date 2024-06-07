import argparse

from tasks.task import Task
from tasks.task_manager import TaskManager


def main():
    task_manager = TaskManager()

    parser = argparse.ArgumentParser(description="To-Do List App")
    subparsers = parser.add_subparsers(dest="command")

    add_parser = subparsers.add_parser("add")
    add_parser.add_argument("title", type=str, help="Title of the task")
    add_parser.add_argument("--description", type=str, help="Description of the task")
    add_parser.add_argument("--priority", type=int, help="Priority of the task")
    add_parser.add_argument("--due_date", type=str, help="Due date of the task (YYYY-MM-DD)")

    update_parser = subparsers.add_parser("update")
    update_parser.add_argument("index", type=int, help="Index of the task to update")
    update_parser.add_argument("--title", type=str, help="New title of the task")
    update_parser.add_argument("--description", type=str, help="New description of the task")
    update_parser.add_argument("--priority", type=int, help="New priority of the task")
    update_parser.add_argument("--due_date", type=str, help="New due date of the task (YYYY-MM-DD)")

    delete_parser = subparsers.add_parser("delete")
    delete_parser.add_argument("index", type=int, help="Index of the task to delete")

    sort_parser = subparsers.add_parser("sort")
    sort_parser.add_argument("by", choices=["priority", "due_date", "creation_date"],
                             help="Sort tasks by this criteria")

    complete_parser = subparsers.add_parser("complete")
    complete_parser.add_argument("index", type=int, help="Index of the task to mark as complete")

    subparsers.add_parser("view", help="View all current tasks")

    args = parser.parse_args()

    if args.command == "add":
        due_date = args.due_date if args.due_date else None
        task = Task(title=args.title, description=args.description, priority=args.priority, due_date=due_date)
        task_manager.add_task(task)
    elif args.command == "update":
        kwargs = {k: v for k, v in vars(args).items() if k not in ["index", "command"] and v is not None}
        task_manager.update_task(args.index, **kwargs)
    elif args.command == "delete":
        task_manager.delete_task(args.index)
    elif args.command == "sort":
        task_manager.sort_tasks(by=args.by)
    elif args.command == "complete":
        task_manager.tasks[args.index].mark_complete()
        task_manager.save_tasks()
    elif args.command == "view":
        print(task_manager)


if __name__ == "__main__":
    main()
