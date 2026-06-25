"""
Project: Professional To-Do List
Team Members: Hedie Navad Mohammad, Neda Hosseinzadeh
Course: Software Engineering Lab
Description: A task management application with Priority, Timestamp, and Filtering features.
"""

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
            try:
                with open(self.filename, "r", encoding="utf-8") as f:
                    # Use 'utf-8' encoding for broader compatibility
                    content = f.read()
                    if content: # Check if file is not empty
                        self.tasks = json.loads(content)
                    else:
                        self.tasks = [] # File is empty, initialize with empty list
            except json.JSONDecodeError:
                print(f"Warning: Could not decode JSON from {self.filename}. Starting with an empty list.")
                self.tasks = [] # Handle corrupted JSON files
            except Exception as e:
                print(f"An error occurred while loading from file: {e}")
                self.tasks = []
        else:
            self.tasks = []

    def save_to_file(self):
        try:
            with open(self.filename, "w", encoding="utf-8") as f:
                # Use 'utf-8' encoding for broader compatibility
                json.dump(self.tasks, f, indent=4, ensure_ascii=False)
                # ensure_ascii=False for better handling of non-ASCII characters
        except Exception as e:
            print(f"An error occurred while saving to file: {e}")

    def add_task(self, name, priority="Medium"):
        if not name or not isinstance(name, str):
            print("Error: Task name cannot be empty and must be a string.")
            return
        if not isinstance(priority, str):
            print("Error: Priority must be a string (e.g., 'High', 'Medium', 'Low').")
            return

        # Normalize priority to ensure consistency
        valid_priorities = ["High", "Medium", "Low"]
        if priority.capitalize() in valid_priorities:
            normalized_priority = priority.capitalize()
        else:
            print(f"Warning: Invalid priority '{priority}'. Setting to 'Medium'.")
            normalized_priority = "Medium"

        task = {
            "task": name,
            "priority": normalized_priority,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.tasks.append(task)
        self.save_to_file()
        print(f"Success: Task '{name}' added with {normalized_priority} priority.")

    def show_tasks(self):
        if not self.tasks:
            print("The list is empty.")
            return
        print("\n--- Current To-Do List ---")
        # Sort tasks by timestamp for a chronological view
        sorted_tasks = sorted(self.tasks, key=lambda x: x.get('timestamp', ''))
        for i, t in enumerate(sorted_tasks, 1):
            # Use .get() with a default value for safer access to keys
            task_name = t.get('task', 'No task name')
            priority = t.get('priority', 'Unknown')
            timestamp = t.get('timestamp', 'Unknown time')
            print(f"{i}. [{priority}] {task_name} (Added: {timestamp})")
        print("--------------------------\n")

    def filter_by_priority(self, priority):
        if not priority or not isinstance(priority, str):
            print("Error: Priority for filtering must be a non-empty string.")
            return

        normalized_filter_priority = priority.lower()
        filtered = [
            t for t in self.tasks
            if t.get('priority', '').lower() == normalized_filter_priority
        ]

        if not filtered:
            print(f"No tasks found with '{priority.capitalize()}' priority.")
            return

        print(f"\n--- {priority.capitalize()} Priority Tasks ---")
        # Sort filtered tasks by timestamp as well
        sorted_filtered_tasks = sorted(filtered, key=lambda x: x.get('timestamp', ''))
        for i, t in enumerate(sorted_filtered_tasks, 1):
            task_name = t.get('task', 'No task name')
            timestamp = t.get('timestamp', 'Unknown time')
            print(f"{i}. {task_name} (Added: {timestamp})")
        print("------------------------------\n")

# Main execution block for testing
if __name__ == "__main__":
    my_todo = TodoList()

    # Adding some sample tasks to demonstrate features
    print("--- Adding Sample Tasks ---")
    my_todo.add_task("Finish Computer Engineering Project", "High")
    my_todo.add_task("Buy groceries", "Low")
    my_todo.add_task("Study for exam", "Medium")
    my_todo.add_task("Plan weekend trip", "Low")
    my_todo.add_task("Prepare presentation", "High")
    my_todo.add_task("Read research paper", "Medium")
    print("--- Sample Tasks Added ---")

    # Show all tasks
    my_todo.show_tasks()

    # Filter by High priority
    my_todo.filter_by_priority("High")

    # Filter by Low priority
    my_todo.filter_by_priority("Low")

    # Example of adding a task with an invalid priority to show warning
    my_todo.add_task("Call mom", "Urgent")
    my_todo.show_tasks()

