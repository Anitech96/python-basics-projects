# to_do_list.py

# List to store tasks
tasks = []

def show_menu():
    print("\n---- TO-DO LIST MENU ----")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Exit")

def add_task():
    task = input("Enter task: ")
    tasks.append({"task": task, "done": False})
    print("✅ Task added.")

def view_tasks():
    if not tasks:
        print("😴 No tasks yet.")
    else:
        print("\n📋 Your Tasks:")
        for index, task in enumerate(tasks, start=1):
            status = "✅ Done" if task["done"] else "❌ Not Done"
            print(f"{index}. {task['task']} - {status}")

def mark_task_done():
    view_tasks()
    if tasks:
        try:
            task_num = int(input("Enter task number to mark as done: "))
            tasks[task_num - 1]["done"] = True
            print("✅ Task marked as done.")
        except (IndexError, ValueError):
            print("⚠️ Invalid task number.")

def delete_task():
    view_tasks()
    if tasks:
        try:
            task_num = int(input("Enter task number to delete: "))
            removed = tasks.pop(task_num - 1)
            print(f"🗑️ Deleted: {removed['task']}")
        except (IndexError, ValueError):
            print("⚠️ Invalid task number.")

# Main program loop
while True:
    show_menu()
    choice = input("Choose an option (1-5): ")

    if choice == '1':
        add_task()
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        mark_task_done()
    elif choice == '4':
        delete_task()
    elif choice == '5':
        print("👋 Goodbye!")
        break
    else:
        print("⚠️ Invalid choice. Please try again.")
