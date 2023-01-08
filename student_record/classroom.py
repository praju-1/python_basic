#!/usr/bin/env python3

#importing modules
import pickle
import os.path as path
from student import Student

'''
Classroom stores student records
and provides -
1.search - search the record of student.
2.serialize - serialize the record in file.
3.deserialize - deserialize the record from file.
4.accept record - accepting input from the user.

'''
class Classroom:
    "This class is used for performing operation"
    def __init__(self, students=0):
        self.on_roll = students
        self.classroom = {}

    def __str__(self):
        try:
            recs = str()
            if len(self.classroom) == 0:
                recs = str(" No records to display")
                return recs

            for student in self.classroom.values():
                recs += str(student)
            return recs
        except Exception as e:
            print(e)

    def search(self):
        "This function search the student record according to roll no."
        try:
            if len(self.classroom) == 0:
                print (" No data entered ")
            else:
                rollno = int(input(" Please enter rollno of student : "))
                if rollno in self.classroom:
                    std = self.classroom[rollno]
                    print (std)
                else:
                    print (" Student record not found")
        except Exception as e:
            print(e)

    def serialize(self):
        "This function serialize the inputed data"
        try:
            if len(self.classroom) == 0:
                print (" No record to serialize. ")
                return

            filename = input(" Please enter filename to save student records : ")
            with open(filename, 'wb') as handle:
                pickle.dump(self.classroom, handle)
            print (" Your records saved succesfully in " + filename)
        except Exception as e:
            print(e)


    def deserialize(self):
        "This function deserialize the inputed data"
        try:
            #opening file for read data
            filename = input(" Please enter filename to read student records : ")
            if path.exists(filename):
                with open(filename, 'rb') as handle:
                    self.classroom = pickle.load(handle)
                    print (" Your records restored succesfully.")
            else:
                print ("File", filename, "does not exist")
        except Exception as e:
            print(e)

    def accept_recs(self):
        "This function access the student data from user."
        try:
            self.on_roll = int(input(" How many student records do you want: "))
            for student in range(0, self.on_roll):
                print ("\n-------- Record", student+1, "----------")
                name = input( " Please enter student name : ")
                rollno = int(input(" Please enter rollno of student : "))
                city = input(" Please enter the city of student : ")
                std = Student(name, rollno, city)
                self.classroom[std.rollno]=std
        except Exception as e:
            print(e)

    def print_recs(self):
        "This function print all record of student."
        try:
            print (self)
        except Exception as e:
            print(e)