# Programmed by: Steven Song
# Started: 02/09/2023
# Finished: 02/13/2023
# Holds infinite loop menu and takes user input and passes it to functions in contacts.py


# import from time library and contacts.py
from contacts import *


# prints welcome, description, and contact
print("Welcome to 'Employee Contact List 2' by: Steven Song") 
print("This program creates a contact list from user input and allows you to print, add, modify, sort and delete contacts.")
print("If you have any questions contact me at Stsong0812@csu.fullerton.edu")


# menu function that prints program options
def menu():
    """
    Menu function that prints the numbers options for the program
    """

    print("""\n*** EMPLOYEE CONTACT MAIN MENU
    1. Print list
    2. Add contact
    3. Modify contact
    4. Delete contact
    5. Sort list by first name
    6. Sort list by last name
    7. Exit the program \n""")


# initialization of empty contacts list
contacts = []


# infinte menu loop
while True:
    menu()      # calls menu function
    # try and except for user input
    try:      
        choice = int(input("Enter a number choice: "))
    except ValueError:
        print("\nInvalid input. Must be an integer between 1-7.")
        continue
    # if/elif for valid user input
    if choice not in range(1,8):
        print("\nInvalid input. Must be an integer between 1-7.")
        continue


    # else if for user choice 1, print contact
    elif choice == 1:
        # checks if contact list is empty
        if len(contacts) == 0:
            print("Contact list is empty, try adding a contact.")
        # else, print formatted contact list
        else:
            print("""\n================== CONTACT LIST ================== 
Index   First Name            Last Name 
======  ====================  ==================== """)
        for i in range(len(contacts)):
            print(f'{str(i):8}{contacts[i][0]:22}{contacts[i][1]:22}')


    # else if for user choice 2, add contact
    elif choice == 2:
        # user input for first and last name
        first_name = input("Enter a first name: ")
        last_name = input("Enter a last name: ")
        print("You entered", first_name, last_name)     # confirmation
        # call add_contact function with contact list as positional parameter
        # and first and last name as keyword parameters
        add_contact(contacts, first=first_name, last=last_name)     


    # else if for user choice 3, modify contact
    elif choice == 3:
        # checks if contact list is empty
        if len(contacts) == 0:
            print("Contact list is empty, try adding a contact.")
        else:   # if list is not empty, prompt user
            # try catch to ensure program does not terminate upon error
            try:
                mod_index = int(input("Enter an index number: "))
            except ValueError:
                print("Invalid input. Input must be an integer.")
                continue
            # checks if user input index is within the range of contact list
            if mod_index not in range(len(contacts)):
                print("Invalid index number. Input must be in range of contacts list.")
                continue
        # prompts for first and last name from user
            mod_first = input("Enter a first name: ")
            mod_last = input("Enter a last name: ")
        print("You decided to modify user at index", mod_index)     # confirmation
        # call modify_contacts function with contact list as a poisitional parameter
        # and index, first and last name as keyword parameters.
        modify_contact(contacts, index=mod_index, first=mod_first, last=mod_last)


    # else if for user choice 4, delete contact
    elif choice == 4:
        # checks if contacts list is empty
        if len(contacts) == 0:
            print("Contact list is empty, try adding a contact.")
        # else, prompt user for index
        else:
        # try catch to ensure program does not terminate upon error
            try:
                delete_index = int(input("Enter an index: "))
            except ValueError:
                print("Invalid input. Input must be an integer.")
                continue
            # checks if user input is in range of contacts list
            if delete_index not in range (len(contacts)):
                print("Invalid index number. Input must be in range of contacts list.")
            # else call delete_contact function and pass contact list as positional parameter
            # index as keyword parameter.
            else:
                print("User at index", delete_index, "has been deleted")     # confirmation
                delete_contact(contacts, index = delete_index)


    # else if for user choice 5, sort contacts by first name
    elif choice == 5:
        # checks if contacts list is empty
        if len(contacts) == 0:
            print("Contact list is empty, try adding a contact.")
        else:
        # calls sort_contact function with contacts list as a positional parameter and
        # column as a keyword paramter. Column = 0 to signify first name sort
            sort_contact(contacts, column=0)
            print("Successfully sorted by first name.")


    # else if for user choice 6, sort contacts by last name
    elif choice == 6:
        # checks if contacts list is empty
        if len(contacts) == 0:
            print("Contact list is empty, try adding a contact.")
        else:
        # calls sort_contact function with contacts list as a positional parameter and
        # column as a keyword parameter. Column = 1 to signify last name sort
            sort_contact(contacts, column=1)
            print("Successfully sorted by last name.")
    

    # else if for user choice 7, exit program
    elif choice == 7:
        print("Have a good day!")   # exit message
        exit()  # exit function that ends program