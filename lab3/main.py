# Programmed by: Steven Song
# Date started: 02/15/23
# This file contains the menu and user input which is used to call the functions in contacts.py

from contacts import *

# initializes empty contacts dictionary
contacts = {}

# infinite loop menu
while True:
    # display menu options
    print("""
    *** EMPLOYEE CONTACT MAIN MENU
\n1. Print contacts
2. Add contact
3. Modify contact
4. Delete contact
5. Sort contacts
6. Find contact
7. Exit the program
""")
    # error catch for user input menu choices
    try:
        # if user input returns an error when type casting to an int...
        # print error message in except
        choice = int(input("Enter menu choice: "))
    except ValueError:
        print("Error. Input must be integer.")
        continue
        # if user input not in range, print error message
    if choice not in range(1, 8):
        print("Error. Input must be in range of menu options. ")
        continue

    # Output for user input choice 1
    elif choice == 1:
        # if the length of contacts is zero, print error message
        if len(contacts) == 0:
            print("Error. Contacts dict is empty.")
        # else, call the print contacts function with contacts as its parameter.
        else:
            print_contacts(contacts)

    # Output for user input choice 2
    elif choice == 2:
        # error catch  and display for phone number input
        try:
            # if type casting of user input phone number return error
            # print error message in except
            phone_number = int(input("Enter phone number: "))
            # if phone number is already in contact, print error
        except ValueError:
            print("Error. Input must be of type: integer.")
            continue
        # display first and last name prompts
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        # else, call add contacts with contacts dictionary and
        # phone_number, first_name, and last_name as respective keyword
        add_contact(contacts, id=phone_number,
                    first=first_name, last=last_name)

    # Output for user input choice 4
    elif choice == 3:
        # if the length of contacts is zero, print error message
        if len(contacts) == 0:
            print("Error. Contacts dict is empty.")
        # else, display first and last name modification prompt
        else:
            # error catch and display for phone number input
            try:
                # if type casting user input phone number into int return error
                # print error message
                phone_number = int(input("Enter phone number: "))
            except ValueError:
                print("Error. Input must be of type: integer.")
                continue
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            # call modify_contact function with contacts dictionary,
            # phone_number, first_name, and last_name as respective keyword
            modify_contact(contacts, id=phone_number,
                        first=first_name, last=last_name)

    # Output for user input choice 4
    elif choice == 4:
        # if the length of contacts is zero, print error message
        if len(contacts) == 0:
            print("Error. Contacts dict is empty")
        # else, call delete_contact function with contact dictionary, and
        # phone_number as keyword parameter 'id'
        else:
        # error catch and display for phone number input
            try:
                # if typecasting user input phone number to int returns error...
                # print error message
                phone_number = int(input("Enter phone number: "))
            except ValueError:
                print("Error. Input must be of type: integer.")
                continue
            delete_contact(contacts, id=phone_number)

    # Output for user input choice 5
    elif choice == 5:
        # if contacts dictionary is empty, print error
        if len(contacts) == 0:
            print("Error. Contacts dict is empty.")
        # else, call sort_contact function with contacts dictionary
        else:
            sort_contact(contacts)

    # Output for user input choice 6
    elif choice == 6:
        # if contacts dictionary is empty, print error message
        if len(contacts) == 0:
            print("Error. Contacts dict is empty.")
        # else, dispaly search string prompt
        else:
            search_string = input("Enter search string: ")
            # call find_contact with contacts dictionary, and
            # search_string as 'find' keyword
            find_contact(contacts, find=search_string)

    # Output for user input choice 7
    elif choice == 7:
        # print exit message and exit
        print("Have a good day!")
        exit()
