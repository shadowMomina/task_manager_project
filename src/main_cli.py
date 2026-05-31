import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from src.task_manager import TaskManager

def main():
    manager = TaskManager()
    os.makedirs("data", exist_ok=True)
    manager.load_from_file("data/tasks.json")

    while True:
        print("\n===== TASK MANAGER =====")
        print("1. Add task")
        print("2. List all tasks")
        print("3. Mark task as done")
        print("4. Remove task")
        print("5. Exit")
        choice = input("Choose: ")

        if choice == "1":
            title = input("Title: ").strip()
            desc = input("Description: ").strip()
            if title:
                tid = manager.add_task(title, desc)
                print(f"Task {tid} added.")
        elif choice == "2":
            for t in manager.list_all():
                print(t)
        elif choice == "3":
            tid = int(input("Task ID: "))
            if manager.mark_done(tid):
                print("Marked done.")
        elif choice == "4":
            tid = int(input("Task ID: "))
            manager.remove_task(tid)
            print("Removed.")
        elif choice == "5":
            manager.save_to_file("data/tasks.json")
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()