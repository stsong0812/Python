# Programmed by: Steven Song
# Started: 02/09/2023
# Finished: 02/14/2023
# Holds functions called in main.py and returns contacts list to main.py


# add_contact function declaration
def add_contact(contacts, /, *, first, last):
    """
    Add contact function allows for the addition of contacts to the list, imports
    the contacts list from main.py as a positional parameter, as well as a first and
    last name input from main.py. After inputs are passed in, the inputs, first and
    last are appended to the contacts list
    """
    # appends the contacts list with user input new first and last name
    contacts.append([first, last])


# modify_contact function declaration
def modify_contact(contacts, /, *, index, first, last):
    """
    Modify contact function passes in contacts list as a positional parameter, as well
    as index, first, and last as keyword parameters. Replaces index of contacts with
    user input first and last names.
    """
    # replaces first and last name with new first and last name at given index
    contacts[index] = [first, last]


# delete_contact function declaration
def delete_contact(contacts, /, *, index):
    """
    Delete contact function that passes in contacts list as a positional parameter and
    index as a keyword parameters. After the function is called with user input index,
    the contacts list will pop the user at the given index.
    """
    # pops the given index of contacts list
    contacts.pop(index)


# sort_contact function declaration
def sort_contact(contacts, /, *, column):
    """
    Sort contacts function that passses the contacts list as a positional parameter and
    the column as a keyword parameter. Using a lambda function, the function called with
    column 0 or 1 will determine which column the sort function will sort by. (Column 
     0 = first name, column 1 = last name)
    """
    # sorts contacts list by first or last name by whether column = 0 or 1
    contacts.sort(key=lambda contact: contact[column])