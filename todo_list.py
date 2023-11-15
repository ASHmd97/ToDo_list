
# Menu message
message = '''1. Add a task
2. View the list of tasks
3. Remove task
4. Exit
: '''

# List to store tasks
tasks = []

# Main loop for the task management program
while True:
    # User input for menu selection
    user_input = input(message)

    if user_input == '1':
        # Add a task
        task = input("Enter a task: ")
        tasks.append(task)
        print("Task added!")

    elif user_input == '2':
        # View the list of tasks
        if len(tasks) > 0:
            for task in tasks:
                print(f"Task: {task}")
        else:
            print("There are no tasks")

    elif user_input == '3':
        # Remove task
        if len(tasks) > 0:
            re_task = input("Enter the task you want to remove: ")
            if re_task in tasks:
                # Confirm the task removal with yes or no
                confirm = input(f"Do you want to remove '{re_task}'? (yes/no): ")
                if confirm.lower() == 'yes':
                    tasks.remove(re_task)
                    print("Task removed.")
                elif confirm.lower() == 'no':
                    print("Removal canceled.")
                else:
                    print("Invalid input. Removal canceled.")
            else:
                print("Task not found.")
        else:
            print("No tasks to remove")

    elif user_input == '4':
        # Exit the program
        print("Goodbye!")
        break

    else:
        # Invalid input
        print("Invalid input")
