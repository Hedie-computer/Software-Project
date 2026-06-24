# To-Do List Project
# Developers: Hedie & Neda

tasks = []

def show_menu():
    print("\n--- To-Do List Menu ---")
    print("1. Add Task")
    print("2. Show Tasks")
    print("3. Exit")

def add_task():
    task = input("Enter the task: ")
    tasks.append(task)
    print("Task added successfully!")

def show_tasks():
    if not tasks:
        print("Your list is empty.")
    else:
        print("\nYour Tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

if __name__ == "__main__":
    while True:
        show_menu()
        choice = input("Choose an option (1-3): ")
        
        if choice == '1':
            add_task()
        elif choice == '2':
            show_tasks()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")
