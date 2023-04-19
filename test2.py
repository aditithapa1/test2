# Phone Directory Management System

# Create an empty dictionary
phoneDirectory = {}

# Function to add a record to the dictionary
def add_record():
    name = input("Enter name: ")
    phone = input("Enter your 10-digit phone number: ")
    phoneDirectory[name] = phone
    print("Record added")

# Function to search a record in the dictionary
def search_record():
    name = input("Enter name to search: ")
    if name in phoneDirectory:
        print(name + ": " + phoneDirectory[name])
    else:
        print("Record not found")

# Function to update a record in the dictionary
def update_record():
    name = input("Enter name: ")
    if name in phoneDirectory:
        phone = input("Enter new 10-digit phone number: ")
        phoneDirectory[name] = phone
        print("Record updated")
    else:
        print("Record not found")

# Function to delete a record from the dictionary
def delete_record():
    name = input("Enter name: ")
    if name in phoneDirectory:
        del phoneDirectory[name]
        print("Record deleted")
    else:
        print("Record not found")

# Main menu loop
while True:
    print("WELCOME TO THE GRANN'S PHONE DIRECTORY MENU\n")
    print("1. Add a record\n2. Search a record\n3. Change a record\n4. Delete a record\n5. Quit\n")
    choice = input("Enter your choice: ")
    
    if choice == '1':
        add_record()
    elif choice == '2':
        search_record()
    elif choice == '3':
        update_record()
    elif choice == '4':
        delete_record()
    elif choice == '5':
        print("Thank you for using the Phone Directory Management System!")
        break
    else:
        print("Invalid choice. Please try again.")
