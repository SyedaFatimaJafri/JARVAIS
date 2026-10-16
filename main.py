
from datetime import datetime
from pathlib import Path
import json

# JARVAS Version 2
DATA_FILE = Path("jarvas_data.json")


def load_data():
    """Load saved notes and tasks from the file."""
    if DATA_FILE.exists():
        try:
            data = json.loads(DATA_FILE.read_text(encoding="utf-8"))
            if isinstance(data, dict):
                if isinstance(data.get("notes"), list) and isinstance(data.get("tasks"), list):
                    return data
        except (json.JSONDecodeError, OSError):
            pass

    return {"notes": [], "tasks": []}


def save_data(data):
    """Save notes and tasks permanently."""
    try:
        DATA_FILE.write_text(
            json.dumps(data, indent=4, ensure_ascii=False),
            encoding="utf-8"
        )
        return True
    except OSError:
        print("Error: Data could not be saved.")
        return False


def show_time():
    print("Current time:", datetime.now().strftime("%I:%M %p"))


def show_date():
    print("Today's date:", datetime.now().strftime("%d-%m-%Y"))


def add_note(data):
    note = input("Write your note: ").strip()

    if not note:
        print("Note cannot be empty.")
        return

    data["notes"].append({
        "text": note,
        "created": datetime.now().strftime("%d-%m-%Y %I:%M %p")
    })

    if save_data(data):
        print("Note saved successfully!")


def view_notes(data):
    if not data["notes"]:
        print("No notes found.")
        return

    print("\n--- YOUR NOTES ---")
    for number, note in enumerate(data["notes"], start=1):
        print(f"{number}. {note['text']}")
        print(f"   Created: {note['created']}")


def delete_note(data):
    view_notes(data)

    if not data["notes"]:
        return

    try:
        number = int(input("Enter note number to delete: "))
        if 1 <= number <= len(data["notes"]):
            removed = data["notes"].pop(number - 1)
            if save_data(data):
                print("Deleted:", removed["text"])
        else:
            print("Invalid note number.")
    except ValueError:
        print("Please enter a valid number.")


def add_task(data):
    task = input("Enter your task: ").strip()

    if not task:
        print("Task cannot be empty.")
        return

    data["tasks"].append({
        "text": task,
        "completed": False,
        "created": datetime.now().strftime("%d-%m-%Y %I:%M %p")
    })

    if save_data(data):
        print("Task added successfully!")


def view_tasks(data):
    if not data["tasks"]:
        print("No tasks found.")
        return

    print("\n--- YOUR TASKS ---")
    for number, task in enumerate(data["tasks"], start=1):
        status = "Completed" if task["completed"] else "Pending"
        print(f"{number}. [{status}] {task['text']}")


def complete_task(data):
    view_tasks(data)

    if not data["tasks"]:
        return

    try:
        number = int(input("Enter task number to complete: "))
        if 1 <= number <= len(data["tasks"]):
            task = data["tasks"][number - 1]

            if task["completed"]:
                print("This task is already completed.")
                return

            task["completed"] = True
            if save_data(data):
                print("Task marked as completed!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


def show_help():
    print("""
Available commands:

time          - Show current time
date          - Show today's date
add note      - Save a note
view notes    - Display saved notes
delete note   - Delete a note
add task      - Create a task
view tasks    - Display all tasks
complete task - Mark a task completed
help          - Show commands
exit          - Close JARVAS
""")


def start_jarvas():
    data = load_data()

    print("=" * 35)
    print("Welcome to JARVAS")
    print("Personal Assistant - Version 2")
    print("=" * 35)

    show_help()

    while True:
        command = input("\nJARVAS > ").strip().lower()

        if command == "time":
            show_time()
        elif command == "date":
            show_date()
        elif command == "add note":
            add_note(data)
        elif command == "view notes":
            view_notes(data)
        elif command == "delete note":
            delete_note(data)
        elif command == "add task":
            add_task(data)
        elif command == "view tasks":
            view_tasks(data)
        elif command == "complete task":
            complete_task(data)
        elif command == "help":
            show_help()
        elif command == "exit":
            print("JARVAS shutting down. Goodbye!")
            break
        elif command == "":
            continue
        else:
            print("Unknown command. Type 'help' to see commands.")


if __name__ == "__main__":
    start_jarvas()
