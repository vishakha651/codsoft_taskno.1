import json

class TodoList:
    def __init__(self):
        self.tasks = self.load_tasks()

    def load_tasks(self):
        try:
            with open('tasks.json', 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    def save_tasks(self):
        with open('tasks.json', 'w') as file:
            json.dump(self.tasks, file)

    def add_task(self, task):
        task_id = len(self.tasks) + 1
        self.tasks[task_id] = {'task': task, 'completed': False}
        self.save_tasks()
        print(f"Task '{task}' added with ID {task_id}.")

    def update_task(self, task_id, new_task):
        if task_id in self.tasks:
            self.tasks[task_id]['task'] = new_task
            self.save_tasks()
            print(f"Task ID {task_id} updated to '{new_task}'.")
        else:
            print(f"Task ID {task_id} not found.")

    def complete_task(self, task_id):
        if task_id in self.tasks:
            self.tasks[task_id]['completed'] = True
            self.save_tasks()
            print(f"Task ID {task_id} marked as completed.")
        else:
            print(f"Task ID {task_id} not found.")

    def display_tasks(self):
        if not self.tasks:
            print("No tasks available.")
            return
        print("\nYour To-Do List:")
        for task_id, task_info in self.tasks.items():
            status = "✔️" if task_info['completed'] else "❌"
            print(f"ID: {task_id} | Task: {task_info['task']} | Status: {status}")
        print()

def main():
    todo_list = TodoList()
    
    while True:
        print("Welcome to the To-Do List App!")
        print("1. Add Task")
        print("2. Update Task")
        print("3. Complete Task")
        print("4. Display Tasks")
        print("5. Exit")
        
        choice = input("Choose an option (1-5): ")
        
        if choice == '1':
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == '2':
            task_id = int(input("Enter the task ID to update: "))
            new_task = input("Enter the new task: ")
            todo_list.update_task(task_id, new_task)
        elif choice == '3':
            task_id = int(input("Enter the task ID to complete: "))
            todo_list.complete_task(task_id)
        elif choice == '4':
            todo_list.display_tasks()
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main() # type: ignore