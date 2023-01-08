#!/usr/bin/env python3

'''
We store student basic information of the student like name. rollno and city in the class.

'''
class Student:
    "This class used for getting info of student"

    def __init__(self, name, rollno, city):
        self.name = name
        self.rollno = rollno
        self.city = city

    def __str__(self):
        "This function return all details of the students"
        try:
            return "\n----------------------------------------\n" + \
                "\nName     : " + self.name + \
                "\nRollno   : " + str(self.rollno) + \
                "\nCity     : " + self.city
        except Exception as e:
            print(e)