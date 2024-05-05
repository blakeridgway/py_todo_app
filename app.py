# Display menu of choices

def show_menu():
    print("Menu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark task as Done")
    print("4. Delete Task")
    print("q. Exit")

def add_task(tasks):
    task = input("Enter your task: ")
    tasks.append(task)
    print("Your task has been added")

def view_task(tasks):
    print("\nTasks:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")

def mark_done(tasks):
    if not tasks:
        print("Nothing was marked done")
        return

    view_task(tasks) # Display tasks
    index = int(input("Enter tasks index to mark as done" )) - 1

    if 0 <= index < len(tasks):
        removed_task = tasks.pop(index)
        print(f"Task '{removed_task} marked as done and removed")
    else:
        print("Invalid task")

def main():
    tasks = [] # Start empty list

    while True:
        show_menu()

        choice = input("Select your choice: ")

        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_task(tasks)
        elif choice == '3':
            mark_done(tasks)
        elif choice == '4':
            print('Not implemented')
        elif choice == 'q':
            print("Exiting app...")
            break
        else:
            print("Invalid selection. Please try again.")

if __name__ == "__main__":
    main()