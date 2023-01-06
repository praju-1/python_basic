#!/usr/bin/env python3

"""
Write a program to create a student record with user input provide display and search functionality.
"""
import sys
from classroom import Classroom
from acts import Actions

#
#register_classroom(act) is function to register
#choice to user.
#

def register_classroom(act):
    cls = Classroom()
    act.register(1, cls.accept_recs, "Enter Student records")
    act.register(2, cls.print_recs, "Display Student records")
    act.register(3, cls.search, "Search Student records")
    act.register(4, cls.serialize, "Save record")
    act.register(5, cls.deserialize, "Read records")
    act.register(6, sys.exit, "Exit")
#
# Entrypoint of program
#
if __name__ == "__main__":
    act = Actions()
    register_classroom(act)
    act.run()

