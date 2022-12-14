#!/usr/bin/env python3
""" Importing modules """
import sys
from contactbook import ContactBook
from action import Actions

def register_contactbook(act):
    """
    A class to represent a register_contactbook
    ...
    Attributes
    ----------
    act : int
        action depend on user choice
    """
    try:
        con = ContactBook()
        "Specifying user choice"
        act.register(1, con.add_contact, "Enter contact details")
        act.register(2, con.display_all, "Display all contact details")
        act.register(3, con.search_contact, "Search contact details")
        act.register(4, con.serialize, "Save contact details")
        act.register(5, con.deserialize, "Read contact details")
        act.register(6, con.remove_contact, "Remove contact details")
        act.register(7, sys.exit, "Exit")
    except Exception as e:
            print(e)

if __name__ == "__main__":
    "Creating class object and calling functions"
    try:
        act = Actions()
        register_contactbook(act)
        act.run()
    except Exception as e:
            print(e)