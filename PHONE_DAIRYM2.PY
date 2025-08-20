import json

# File ka naam jahan contacts save honge
FILE_NAME = 'contacts.json'

def load_contacts():
    """Loads contacts from the JSON file."""
    try:
        # 'r' mode me file open karein, 'with' block se file automatically close ho jayegi
        with open(FILE_NAME, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        # Agar file nahi milti ya data corrupted hai, to empty dictionary return karein
        return {}

def save_contacts(data):
    """Saves contacts to the JSON file."""
    # 'w' mode me file open karein, jo naya data write karega
    with open(FILE_NAME, 'w') as file:
        # indent=4 se file ka data padhne me asaan ho jayega
        json.dump(data, file, indent=4)

# Program shuru hone par contacts load karein
phone_directory = load_contacts()

def add_contact():
    """Adds a new contact to the directory."""
    name = input("Enter the name of the contact: ")
    number = input("Enter the number of the contact: ")
    phone_directory[name] = number
    save_contacts(phone_directory)  # Data ko save karein
    print(f"Contact '{name}' added successfully!")

def view_all_contacts():
    """Displays all contacts in the directory."""
    if not phone_directory:
        print("Your contact list is empty.")
    else:
        print("\n--- All Contacts ---")
        for name, number in phone_directory.items():
            print(f"Name: {name}, Number: {number}")

def search_contact():
    """Searches for a contact by name."""
    search_name = input("Enter the name to search: ")
    if search_name in phone_directory:
        print(f"Name: {search_name}, Number: {phone_directory[search_name]}")
    else:
        print(f"Contact '{search_name}' not found.")

def delete_contact():
    """Deletes a contact and saves the changes."""
    delete_name = input("Enter the name of the contact to delete: ")
    if delete_name in phone_directory:
        del phone_directory[delete_name]
        save_contacts(phone_directory)  # Changes ko save karein
        print(f"Contact '{delete_name}' deleted successfully!")
    else:
        print(f"Contact '{delete_name}' is not in your contact list.")

def exit_app():
    """Exits the application."""
    print("Thank you for using the Contact Book. Goodbye!")

while True:
    print("\n--- Contact Book Menu ---")
    print("1. Add a Contact")
    print("2. View All Contacts")
    print("3. Search a Contact")
    print("4. Delete a Contact")
    print("5. Exit")

    try:
        choice = int(input("Enter your choice: "))
        if choice == 1:
            add_contact()
        elif choice == 2:
            view_all_contacts()
        elif choice == 3:
            search_contact()
        elif choice == 4:
            delete_contact()
        elif choice == 5:
            exit_app()
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")