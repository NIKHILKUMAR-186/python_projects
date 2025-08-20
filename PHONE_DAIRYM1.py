phone_diry = {}

def addcontact(name , number):
    phone_diry[f"{name}"] = f"{number}"

def view_all_contact():
    for name , number in phone_diry.items():
        print(f"{name}: {number}")


def search():
    try:
        if search_name in phone_diry:
            print(f" {search_name} : {phone_diry.get(search_name)}")
        else:
            print("enter a valid contact name") 
    except ValueError:
        print("enter a valid name")

def delete_contact(name):
    if name in phone_diry:
        phone_diry.pop(name)
    else:
        print(f"{name} is not in your contact list!")

def exit_dairy():
    print("thanku for using!!")
    return False


while True:
    print("1. Add a Contact:")
    print("2. View All Contacts")
    print("3. Search a Contact:")
    print("4. Delete a Contact")
    print("5. Exit")



    try:
        choice = int(input("enter your choice: "))
        if (choice== 1):
            try:
                name = input("enter the name of a contact you want to add: ")
                number = int(input("enter the number of a contact you want to add: "))
                addcontact(name , number) 
            except ValueError:
                print("enter a valid details")   
        elif (choice == 2):
            view_all_contact()
        elif (choice==3):
            search_name = input("enter the name you want to search: ")            
            search()
        elif (choice == 4):
            delete_contact_name = input("enter the name of  contact you want to delete: ")
            delete_contact(delete_contact_name)
        elif (choice== 5):
            exit_dairy()
            break
        else:
            print("enter a valid choice between 1 and 5")

    except ValueError:
        print("enter a valid details!!")


