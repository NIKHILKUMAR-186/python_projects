to_do_list  = []


while True:
    print("\nto do list menu ")
    print("1 = add a task")
    print("2 = view tasks")
    print("3 = mark a task as completed ")
    print("4 = exit ")


    try:
        choice = int(input("enter you choice: "))

        if (choice == 1):
            task = input("enter a task to add : ")
            to_do_list.append(task )
            print("task added succesfully!")

        elif (choice == 2):
            if not to_do_list:
                print("Your to-do list is empty.")
            else:
                print("\nYour tasks:")
                for index, task in enumerate(to_do_list, 1):
                    print(f"task{index}. {task}")
            # print(to_do_list)

        elif (choice== 3):
            try:
                for index, task in enumerate(to_do_list, 1):
                    print(f"task{index}. {task}")
                task_number = int(input("Enter the  task number to mark as completed: "))
                if (1<task_number <= len(to_do_list)):
                    # for index, task in enumerate(to_do_list, 1):
                    to_do_list.pop(task_number -1 )
                    print(f"the task {task} is marked completed !")
                else:
                    print("enter the correct task number !")
            except ValueError:
                print("enter a valid task number")
        elif (choice == 4):
            print("thanku for using TO DO LIST")
            break
        else:
            print("enter a valid input between 1 and 4")

    except ValueError:
        print("Invalid input. Please enter a valid number for your choice.")

    
