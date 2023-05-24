# Programmed by: Steven Song
# Date started: 02/15/23
# This file contains the print, add, modify, delete, sort, and find contact functions called
# from main.py.

def print_contacts(contacts, /):
    """
    Print contacts function that passes the contact dictionary as a positional parameter 
    when called from main.py. The information stored in the dictionary is then formatted
    and printed back to the user. Printed last name, first name, then phone number.
    """
    print("""==================== CONTACT LIST ==================== 
Last Name             First Name            Phone 
====================  ====================  ==========""")
    # loops throuh every element in contact
    for i in contacts:
        # prints every key and values with a designated width
        print(f'{contacts[i][1]:22}{contacts[i][0]:22}{str(i):8}')


def add_contact(contacts, /, *, id, first, last):
    """
    Add contact function that passes the contact dictionary as a positional parameter
    and id, first and last name as keyword parameters when called in main.py. If id
    already exists within contacts dictionary, return an error string. Else, a contact
    with the user input ID will be added, with the first and last name provided.
    """
    # Check if the ID already exists in the contacts dictionary
    if id in contacts:
        return "Error. Phone number already in contacts."
    else:
        contacts[id] = first, last
        # Return the added contact
        return "Added:", first, last + "."


def modify_contact(contacts, /, *, id, first, last):
    """
    Modify contact function that takes the contact dictionary as a positional parameter
    and id, first, and last as keyword parameters when called from main.py. If id is not
    found within the contacts list, return an error string. Else, modify the contact in
    the contacts dictionary with the specified ID, updating the first and last name.
    """
    if id not in contacts:
        return "Error. Phone number not found in contacts."
    else:
        # Modify the contact with the specified ID
        contacts[id] = first, last
        # Return the modified contact
        return "Modified contact:", first, last


def delete_contact(contacts, /, *, id):
    """
    Delete contact function that takes the contact dictionary as a positional parameter,
    and id as a keyword parameter. If the ID does not exist within the contacts list,
    return an error string. Else, remove the contact with the specified ID from the
    contacts dictionary.
    """
    if id not in contacts:
        return "Error. Phone number not found in contacts."
    else:
        # Remove the contact with the specified ID
        contacts.pop(id)
        # Return the deleted contact ID
        return "Deleted Contact:", id


def sort_contact(contacts, /):
    """
    Sort contact function that takes the contact dictionary as a positional paramter.
    The function will sort the elements in the contacts dictionary in ascending order
    by last name, then by first name and returns the sorted dictionary.
    """
    # sorts original dictionary by last name first, then first name, and initializes it
    # to sorted_contacts
    sorted_contacts = (
        sorted(contacts.items(), key=lambda x: (x[1][1], x[1][0])))
    # empty the original contacts dictionary
    contacts.clear()
    # update the empty contacts dictionary with the elements in sorted_conctacts dictionary
    contacts.update(sorted_contacts)
    # return contacts dictionary
    return contacts


def find_contact(contacts, /, *, find):
    """
    Find contact function that takes contacts dictionary as a positional parameter and
    find as a keyword parameter. Then the function iterates through the dictionary to 
    find the user input string to search by.
    """
    # initialize new 'find' dictionary
    find_dict = {}
    # checks if 'find' is a numeric value
    if find.isnumeric():
        # typecasts find into an int
        find = int(find)
        # if find is in the keys of contacts...
        if find in contacts:
            # add find key and value to find dictionary
            find_dict[find] = contacts[find]
            # print head
            print("""================== FOUND CONTACT(S) ================== 
Last Name             First Name            Phone 
====================  ====================  ========== """)
            # iterate through the new dictionary, sort and print print
            for i in sorted(find_dict.values(), key=lambda x: (x[0], x[1])):
                # print the sorted find dictionary with designated widths
                print(f'{i[1]:22}{i[0]:22}{str(find):8}')
    # if find is not a numeric value
    else:
        # iterate through values of contacts dictionary
        for key, value in contacts.items():
            # check if the find string is in the keys or values of the dictionary
            if str(find) in str(key) or find in value:
                # set the key to the value in find dictionary
                find_dict[key] = value
        # print head
        print("""================== FOUND CONTACT(S) ================== 
Last Name             First Name            Phone 
====================  ====================  ========== """)
        # iterate through the new dictionary, sort and print
        for i in sorted(find_dict.values(), key=lambda x: (x[0], x[1])):
            print(
                f'{i[1]:22}{i[0]:22}{list(contacts.keys())[list(contacts.values()).index(i)]:8}')
