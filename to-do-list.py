# Simple To-Do List Application

# Initialize an empty to-do list
todo_list = []

# Function to add a task to the to-do list
i=1
n=1
def add_task(task):
    todo_list.append(task)
    print(f"Task '{task}' added to the to-do list.")

# Function to remove a task from the to-do list
def remove_task(task):
    if task in todo_list:
        todo_list.remove(task)
        print(f"Task '{task}' removed from the to-do list.")
    else:
        print(f"Task '{task}' not found in the to-do list.")

# Function to display the current to-do list
def display_todo_list():
    if len(todo_list) == 0:
        print("Your to-do list is empty.")
    else:
        print("Your to-do list:")
        for index, task in enumerate(todo_list, start=1):
            print(f"{index}. {task}")
          
# Function to reorder the to-do list
def reorder_todo_list():
  display_todo_list()
  current_task = input("Enter the task you want to reorder: ")
  new_position = int(input("Enter the new position:"))
  if current_task in todo_list:
    todo_list.remove(current_task)
    todo_list.insert(new_position - 1, current_task)
    print("Task", current_task, "reordered to position", new_position)
  else:
    print("Task", current_task, "not found in the todo list.")

# Function to Change the to-do list
def change_todo_list():
  display_todo_list()
  current_task2 = (input("Enter the task that you want to change: "))
  new_task2 = (input("Enter the new task: "))
  if current_task2 in todo_list:
    todo_list.insert(todo_list.index(current_task2), new_task2) 
    todo_list.remove(current_task2)
    print("Task", current_task2, "changed to task", new_task2)
  else:
    print("Task", current_task2, "not found in the todo list")
while True:
    print("\nWelcome to the To-Do List Application!")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. Display To-Do List")
    print("4. Re-order")
    print("5. Change")
    print("6. Quit")
    choice = input("Please enter your choice: ")
    if choice == "1":
        task = input("Enter the task you want to add: ")
        add_task(task)
    elif choice == "2":
        task = input("Enter the task you want to remove: ")
        remove_task(task)
    elif choice == "3":
        display_todo_list()
    elif choice == "4":
        reorder_todo_list()
    elif choice == "5":
        change_todo_list()
    elif choice == "6":
        print("Thank you for using the To-Do List Application. Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option.")
