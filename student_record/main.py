#!/usr/bin/env python3

"""
Write a program to create a student record with user input provide display and search functionality.
"""
#Importing data from another file
import sys
from classroom import Classroom
from acts import Actions

#
#register_classroom(act) is function to register
#choice to user.
#

def register_classroom(act):
    try:
        "Object creation of class"
        cls = Classroom()
        #Calling methods of the respective classes
        act.register(1, cls.accept_recs, "Enter Student records")
        act.register(2, cls.print_recs, "Display Student records")
        act.register(3, cls.search, "Search Student records")
        act.register(4, cls.serialize, "Save record")
        act.register(5, cls.deserialize, "Read records")
        act.register(6, sys.exit, "Exit")
    except Exception as e:
            print(e)

if __name__ == "__main__":
    "Execution of program starts from here"
    act = Actions()
    register_classroom(act)
    act.run()