#!/usr/bin/env python3

'''
We store student basic information of the student like name. rollno and city in the class.

'''
class Student:

    def __init__(self, name, rollno, city):
        self.name = name
        self.rollno = rollno
        self.city = city

    def __str__(self):
        return "\n----------------------------------------\n" + \
            "\nName     : " + self.name + \
            "\nRollno   : " + str(self.rollno) + \
            "\nCity     : " + self.city

