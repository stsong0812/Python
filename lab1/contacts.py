# Programmed by: Steven Song
# 02/02/2023
# Contains contacts list and functions used in main.py


# empty list for storing contacts
contacts = []


# function that prints the list of contacts
def print_list():
    # checks if current list is empty
    if len(contacts) == 0:
        print("\n Your contacts list is empty")
    # if not, print list
    else:
        print("""\n================== CONTACT LIST ================== 
Index   First Name            Last Name 
======  ====================  ==================== """)
        # loops through items in contacts list and prints them formatted
        for i in range(len(contacts)):
            print(f'{str(i):8}{contacts[i][0]:22}{contacts[i][1]:22}')


# function that adds contacts to the contacts list
def add_contact():
    # prompts user for fist and last names and stores them in two variables
    firstName = input("\n Enter first name: ")
    lastName = input(" Enter last name: ")
    # prints confirmation of name entered
    print("\nYou entered: " + firstName + " " + lastName)
    contacts.append([firstName, lastName])  # appends names to contacts list


# function that allows modification of an employee in contacts list
def modify_contact():
    # checks if current list is empty
    if len(contacts) == 0:
        print("\nYour contacts list is empty")
        return False
    # type cast user input into integer
    modIndex = int(input("\n Enter the index number: "))
    # checks if user input index is in list
    if modIndex > len(contacts):
        print("\nInvalid index number")
    else:
        # if index is in list, creates new first and last name variables from user input
        newFirst = input("\n Enter new First Name: ")
        newLast = input(" Enter new Last Name: ")
        # confrims new user input names
        print("\nYou entered: " + newFirst + " " + newLast)
        # replaces existing index with items from new index
        contacts[modIndex] = [newFirst, newLast]


# function that allows the deletion of an employee from list
def delete_contact():
    # checks if current list is empty
    if len(contacts) == 0:
        print("\nYour contacts list is empty")
        return False
    delIndex = int(input("\n Enter the index number: "))
    # checks if user input index is in list
    if delIndex > len(contacts):
        print("\nInvalid index number")
    # if index is in list, continue
    else:
        contacts.pop(delIndex)  # removes contact from list
        # confirmation of successful instruction
        print("\nContact", delIndex, "has successfully been deleted")


# function that exits program with message
def exit_program():
    print("Have a good day!")
    exit()  # exit function