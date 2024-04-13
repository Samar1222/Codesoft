import pickle
import os

class Task:
    def __init__(self, description, completed=False):
        self.description = description
        self.completed = completed

class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def view_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
        else:
            for i, task in enumerate(self.tasks, start=1):
                status = "✓" if task.completed else "✗"
                print(f"{i}. [{status}] {task.description}")

    def mark_completed(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            self.tasks[task_index - 1].completed = True
        else:
            print("Invalid task index.")

    def delete_task(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            del self.tasks[task_index - 1]
        else:
            print("Invalid task index.")

    def save_to_file(self, filename):
        with open(filename, "wb") as f:
            pickle.dump(self.tasks, f)

    def load_from_file(self, filename):
        if os.path.exists(filename):
            with open(filename, "rb") as f:
                self.tasks = pickle.load(f)

def main():
    todo_list = TodoList()
    filename = "todo_list.pkl"
    todo_list.load_from_file(filename)

    while True:
        print("\n==== To-Do List ====")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Save and Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            todo_list.view_tasks()
        elif choice == "2":
            description = input("Enter task description: ")
            task = Task(description)
            todo_list.add_task(task)
        elif choice == "3":
            todo_list.view_tasks()
            task_index = int(input("Enter task index to mark as completed: "))
            todo_list.mark_completed(task_index)
        elif choice == "4":
            todo_list.view_tasks()
            task_index = int(input("Enter task index to delete: "))
            todo_list.delete_task(task_index)
        elif choice == "5":
            todo_list.save_to_file(filename)
            print("To-Do List saved. Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
