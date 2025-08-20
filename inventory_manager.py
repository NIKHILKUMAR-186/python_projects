todo_list = []

def add_task(task):
    todo_list.append(task)
    print("task added succesfully!")


def view_list():
    if not todo_list:
        print("your to do list is empty! ")
    else:
        print("\nyour tasks: ")
        for index , task in enumerate(todo_list , 1):
            print(f"task {index} = {task}")
        
def completed(task_number):
    if not todo_list:
        print("your todo list is empty . no task to complete.")
        return
    view_list()
    try:
        for index , task in enumerate(todo_list , 1):
            print(f"task{index}. {task}")
        if (0<task_number <= len(todo_list)):
            task = todo_list.pop(task_number - 1)
            print(f"the task {task} is marked completed !")
        else:
            print("enter the choice in range")
    except ValueError:
        print("invalid task number !")

def exit():
    print("goodbye!")
    return False
    

while True:
    print("\nto do list menu ")
    print("1 = add a task")
    print("2 = view tasks")
    print("3 = mark a task as completed ")
    print("4 = exit ")

    try:
        choice = int(input("enter you choice: "))

        if (choice == 1):
            task = input("enter the task you want to add : ")
            add_task(task)
        elif (choice == 2):
            view_list()
        elif (choice == 3):
            task_number = int(input("enter the task number you want to remove from the todo list : " ))
            completed(task_number)
        elif(choice == 4):
            exit()
            break
        else:
            print("enter the valid choice from 1,2,3,4 : ")
    except ValueError:
        print("enter the valid choice")


