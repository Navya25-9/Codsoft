class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})

    def view_tasks(self):
        if self.tasks:
            print("To-Do List:")
            for i, task in enumerate(self.tasks, start=1):
                status = "Done" if task["completed"] else "Pending"
                print(f"{i}. {task['task']} - {status}")
        else:
            print("No tasks found!")

    def mark_task_completed(self, task_index):
        try:
            self.tasks[task_index - 1]["completed"] = True
            print("Task marked as completed.")
        except IndexError:
            print("Invalid task index!")

    def delete_task(self, task_index):
        try:
            del self.tasks[task_index - 1]
            print("Task deleted.")
        except IndexError:
            print("Invalid task index!")


def main():
    todo_list = ToDoList()
    while True:
        print("\n1. Add Task\n2. View Tasks\n3. Mark Task as Completed\n4. Delete Task\n5. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            task = input("Enter task: ")
            todo_list.add_task(task)
        elif choice == "2":
            todo_list.view_tasks()
        elif choice == "3":
            try:
                task_index = int(input("Enter task index to mark as completed: "))
                todo_list.mark_task_completed(task_index)
            except ValueError:
                print("Invalid input! Please enter a valid integer for task index.")
        elif choice == "4":
            try:
                task_index = int(input("Enter task index to delete: "))
                todo_list.delete_task(task_index)
            except ValueError:
                print("Invalid input! Please enter a valid integer for task index.")
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please choose again.")


if __name__ == "__main__":
    main()

