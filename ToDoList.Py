print("=" * 50)
print("          TO-DO LIST APPLICATION")
print("=" * 50)

tasks = []

while True:
    print("\nMENU")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Search Task")
    print("6. Count Tasks")
    print("7. Exit")

    choice = input("Enter your choice (1-7): ")

    if choice == "1":
        task = input("Enter new task: ")
        tasks.append(task)
        print("Task added successfully!")

    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            print("\nCurrent Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(str(i) + ". " + task)

    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks to update.")
        else:
            for i, task in enumerate(tasks, start=1):
                print(str(i) + ". " + task)

            num = int(input("Enter task number to update: "))
            if 1 <= num <= len(tasks):
                new_task = input("Enter new task: ")
                tasks[num - 1] = new_task
                print("Task updated successfully!")
            else:
                print("Invalid task number.")

    elif choice == "4":
        if len(tasks) == 0:
            print("No tasks to delete.")
        else:
            for i, task in enumerate(tasks, start=1):
                print(str(i) + ". " + task)

            num = int(input("Enter task number to delete: "))
            if 1 <= num <= len(tasks):
                removed = tasks.pop(num - 1)
                print(removed, "deleted successfully!")
            else:
                print("Invalid task number.")

    elif choice == "5":
        search = input("Enter task to search: ")

        if search in tasks:
            print("Task found!")
        else:
            print("Task not found.")

    elif choice == "6":
        print("Total number of tasks:", len(tasks))

    elif choice == "7":
        print("Thank you for using the To-Do List Application.")
        break

    else:
        print("Invalid choice. Please enter a number from 1 to 7.")
