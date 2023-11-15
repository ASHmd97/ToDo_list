class TodoList:
    def __init__(self):
        """
        Initialize a TodoList object with an empty list for tasks.
        """
        self.tasks = []

    def add_task(self, name, details):
        """
        Add a task to the todo list.

        Parameters:
        - name (str): The name of the task.
        - details (str): Details or description of the task.
        """
        task = {'name': name, 'details': details}
        self.tasks.append(task)
        print(f"Task '{name}' added.")

    def view_tasks(self):
        """
        View all tasks in the todo list.
        """
        if self.tasks:
            print("Tasks:")
            for i, task in enumerate(self.tasks, start=1):
                print(f"{i}. Name: {task['name']}, Details: {task['details']}")
        else:
            print("No tasks in the list.")

    def remove_task(self, task_index):
        """
        Remove a task from the todo list based on the given index.

        Parameters:
        - task_index (int): The index of the task to be removed.
        """
        if 1 <= task_index <= len(self.tasks):
            removed_task = self.tasks.pop(task_index - 1)
            print(f"Task '{removed_task['name']}' removed.")
        else:
            print("Invalid task index.")

# Create a TodoList instance
todo_list = TodoList()

while True:
    print("\n1. Add a task\n2. View tasks\n3. Remove a task\n4. Exit")
    choice = input("Enter your choice (1/2/3/4): ")

    if choice == '1':
        name = input("Enter the name of the task: ")
        details = input("Enter details of the task: ")
        todo_list.add_task(name, details)

    elif choice == '2':
        todo_list.view_tasks()

    elif choice == '3':
        todo_list.view_tasks()
        if todo_list.tasks:
            task_index = int(input("Enter the task number to remove: "))
            todo_list.remove_task(task_index)

    elif choice == '4':
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please enter 1, 2, 3, or 4.")
