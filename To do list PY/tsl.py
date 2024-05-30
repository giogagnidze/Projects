def add_task(todo_list):
    task = input("Enter the task to add: ")
    todo_list.append(task)
    print("Task added successfully!")

def remove_task(todo_list):
    if len(todo_list) == 0:
        print("The to-do list is empty.")
        return

    print("Current to-do list:")
    for i in range(len(todo_list)):
        print(f"{i + 1}. {todo_list[i]}")

    index = int(input("Enter the index of the task to remove: ")) - 1
    if 0 <= index < len(todo_list):
        removed_task = todo_list.pop(index)
        print(f"Task '{removed_task}' removed successfully!")
    else:
        print("Invalid index!")
        
def display_todo_list(todo_list):
    if len(todo_list) == 0:
        print("The to-do list is empty.")
    else:
        print("To-do list:")
        for i in range(len(todo_list)):
            print(f"{i + 1}. {todo_list[i]}")

def main():
    todo_list = []
    
    while True:
        print("\nTO-DO LIST MENU:")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Display To-Do List")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_task(todo_list)
        elif choice == '2':
            remove_task(todo_list)
        elif choice == '3':
            display_todo_list(todo_list)
        elif choice == '4':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 4.")           
main()
