import json
import os
from datetime import datetime

class TodoList:
    def __init__(self, filename="data.json"):
        self.filename = filename
        self.tasks = []
        self.load_from_file()

    def load_from_file(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as f:
                self.tasks = json.load(f)
        else:
            self.tasks = []

    def save_to_file(self):
        with open(self.filename, "w") as f:
            json.dump(self.tasks, f, indent=4)

    def add_task(self, name, priority="Medium"):
        # Create a new task with timestamp and priority
        task = {
            "task": name,
            "priority": priority,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.tasks.append(task)
        self.save_to_file()
        print(f"Success: Task '{name}' added with {priority} priority.")

    def show_tasks(self):
        if not self.tasks:
            print("The list is empty.")
            return
        print("\n--- Current To-Do List ---")
        for i, t in enumerate(self.tasks, 1):
            print(f"{i}. [{t['priority']}] {t['task']} (Added: {t['timestamp']})")
        print("--------------------------\n")

    def filter_by_priority(self, priority):
        filtered = [t for t in self.tasks if t['priority'].lower() == priority.lower()]
        if not filtered:
            print(f"No tasks found with {priority} priority.")
            return
        print(f"\n--- {priority.capitalize()} Priority Tasks ---")
        for i, t in enumerate(filtered, 1):
            print(f"{i}. {t['task']} (Added: {t['timestamp']})")
        print("------------------------------\n")

# Main execution block for testing
if __name__ == "__main__":
    my_todo = TodoList()
    # Adding some sample tasks to demonstrate features
    my_todo.add_task("Finish Computer Engineering Project", "High")
    my_todo.add_task("Buy groceries", "Low")
    my_todo.add_task("Study for exam", "Medium")
    
    # Show all
    my_todo.show_tasks()
    
    # Filter high priority
    my_todo.filter_by_priority("High")
