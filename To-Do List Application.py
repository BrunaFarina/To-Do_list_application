from time import sleep

list_task = []

def to_do_list():
    choice = ""
    print("Welcome to To-Do List Application!")
    while choice != "5" or choice == "Exit":
        sleep(1)
        print("1. Add task")
        print("2. View tasks")
        print("3. Mark task as completed")
        print("4. Remove task")
        print("5. Exit")
        sleep(1)
        choice = input("Enter your choice: ")
        if choice == "1":
            sleep(0.5)
            task = input("Enter task description: ")
            list_task.append(task)
        elif choice == "2" or choice == "View task":
                print("================")
                print("Your to-do list:")
                for i, name in enumerate(list_task, 1):
                    print(i, name)
                print("================")
        elif choice == "3" or choice == "Mark task as completed":
            completed_task = input("Which task (number) do you want to mark as completed? ")
            list_task[int(completed_task) - 1] = list_task[int(completed_task) - 1] + " - COMPLETED"
        elif choice == "4" or choice == "Remove task":
            task_to_remove = input("Which task (number) do you want to remove? ")
            del list_task[int(task_to_remove) - 1]
    else:
        print("Bye!")
to_do_list()
