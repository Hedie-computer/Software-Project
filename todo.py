class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"✅ Added: {task}")

    def show_tasks(self):
        print("\n--- Current Tasks ---")
        for i, t in enumerate(self.tasks, 1):
            print(f"{i}. {t}")

    def remove_task(self, index):
        if 0 < index <= len(self.tasks):
            removed = self.tasks.pop(index - 1)
            print(f"🗑️ Removed: {removed}")
        else:
            print("⚠️ Invalid index!")

# --- Main Program ---
my_list = TodoList()
my_list.add_task("Set up GitHub Repo (By Hedie)")
my_list.add_task("Implement Logic (By Neda)")
my_list.show_tasks()
