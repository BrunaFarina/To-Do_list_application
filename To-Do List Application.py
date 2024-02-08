list_task = []

def to_do_list():
    choice = ""
    print("Welcome to To-Do List Application!")
    while choice != "5" or choice == "Exit":
        print("1. Add task")
        print("2. View tasks")
        print("3. Mark task as completed")
        print("4. Remove task")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            task = input("Enter task description: ")
            list_task.append(task)
        elif choice == "2" or choice == "View task":
                print("================")
                print("Your to-do list:")
                for i, name in enumerate(list_task):
                    print(i, name)
                print("================")
        elif choice == "3" or choice == "Mark task as completed":
            completed_task = input("Which task (number) do you want to mark as completed? ")
            list_task[int(completed_task)] = list_task[int(completed_task)] + " - COMPLETED"
        elif choice == "4" or choice == "Remove task":
            task_to_remove = input("Which task (number) do you want to remove? ")
            del list_task[int(task_to_remove)]
    else:
        print("Bye!")
to_do_list()
