# Programmed by: Steven Song
# 02/02/2023
# Contains menu for contacts.py


# imports functions from contacts
from contacts import *


# prints welcome, description, and contact
print("""
\nWelcome to 'Employee Contacts List' by Steven Song!
This program shows a list of employees and allows for their addition, deletion, and modification.
Feel free to contact me at stsong0812@csu.fullerton.edu if you need assistance.
""")


# function that prints menu options
def options():
    print("""\n---------------------------------------
    *** EMPLOYEE CONTACT MAIN MENU
        1. Print list
        2. Add contact
        3. Modify contact
        4. Delete contact
        5. Exit the program 
---------------------------------------\n""")


# creates an infinite loop
while True:
    options()
    # type cast user input into an integer
    option = input("Enter a menu choice: ")
    # checks what option user chose
    if option == "1":
        print_list()        # calls print list function in contacts.py
    elif option == "2":
        add_contact()       # calls print list function in contacts.py
    elif option == "3":
        modify_contact()    # calls modify contact function in contacts.py
    elif option == "4":
        delete_contact()    # calls delete contact function in contacts.py
    elif option == "5":
        exit_program()      # calls exit program function in contacts.py
    else:                   # else statement for any other input
        print("\nInvalid menu option")