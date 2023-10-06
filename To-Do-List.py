# To-Do List App in Python

# Create an empty list to store tasks
tasks = []

# Function to add a task to the list
def add_task(task):
    tasks.append(task)
    print(f"Task '{task}' has been added to the list.")
    
    #function to remove a task from the list
    def remove_task(task):
        if task in tasks:
            tasks.remove(task)
            print(f"Task '{task}' has been removed from the list.")
        else:
            print(f"Task '{task}' not found in the list.")
            
#function to show all task in the list
def show_tasks():
    if tasks:
        print("Task in the To-Do List:")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")
        else:
            print("The To-Do List is empty.")
            
# Main loop for the To-Do List App
while True:
    print("To-Do List App Menu:")
    print("1. Add a task")
    print("2. Remove a task")
    print("3. Show tasks")
    print("4. Quit")
    
    choice = input("Enter your choice (1/2/3/4 )")
    
    if choice == '1': 
        task= input("Enter the task to add: ")
        add_task(task)
    elif choice == '2':
        task= input("Enter the task to remove:")
        remove_task(task)
    elif choice == '3' :
        show_tasks()
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please choose a option.")
        
        


    