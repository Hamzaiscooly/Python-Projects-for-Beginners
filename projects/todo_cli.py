# Simple CLI To-Do List

tasks = []

def show_menu():
    print("\n1. Add Task\n2. View Tasks\n3. Quit")

while True:
    show_menu()
    choice = input("Choose an option: ")

    if choice == "1":
        task = input("Enter a new task: ")
        tasks.append(task)
        print("Task added.")
    elif choice == "2":
        print("\nYour Tasks:")
        for i, t in enumerate(tasks, 1):
            print(f"{i}. {t}")
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")