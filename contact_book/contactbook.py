#!/usr/bin/env python3
""" Importing module """
import pickle
import os.path as path
from contact import Contact
import re

class ContactBook:
    """
    A class to represent a contactbook
    ...
    Attributes
    ----------
    contacts : int
        contact from the contact book

    Methods
    -------
    add_contact():
        Adding contact details in contactbook
    display_all():
        Display all records of stored contacts
    search_contact():
        Search the contact for user
    serialize():
        Save contact records in file provided by user
    deserialize():
        Read all records from file
    remove_contact():
        Remove contact from a record
    """
    def __init__(self, contacts=0):
        """
        Constructs all the necessary attributes for the contactbook object
        """
        self.on_book = contacts
        self.contactbook = {}

    def __str__(self):
        recs = str()
        if len(self.contactbook) == 0:
            recs = str(" No records to display")
            return recs
        
        for contact in self.contactbook.values():
            recs += str(contact)
        return recs

    def add_contact(self):
        """ Adding information for contact """
        self.on_book = int(input(" How many contact records do you want: "))
        for contact in range(0, self.on_book):
            print ("\n-------- Record", contact+1, "----------")
            name = str(input(" Please enter name : "))
            number = int(input(" Please enter 10 digit contact number : "))
            city = str(input(" Please enter name of city : "))
            email = str(input(" Please enter the email_id : "))
            """ validating email_id """
            if not re.match(r"^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$",email):
                print("\n Please enter valid email_id ")

            cont = Contact(name, number, city, email)
            self.contactbook[cont.number]=cont

    def display_all(self):
        """ Display all entered contact records """
        print(self)

    def search_contact(self):
        """ Searching contacts for an user """
        if len(self.contactbook) == 0:
            print (" No data entered ")
        else:
            number = int(input(" Please enter number for search : "))
            if len(str(number)) < 10:
                print (" Invalid number. Please enter valid number ")
            elif number in self.contactbook:
                cont = self.contactbook[number]
                print (cont)
            else:
                print (" contact record not found ")
  
    def serialize(self):
        """ save contact records in file provided by user """
        if len(self.contactbook) == 0:
            print (" No record to serialize. ")
            return
        
        filename = input(" Please enter filename to save contacts records : ")
        """opening file in binary mode for writing"""
        with open(filename, 'wb') as handle:
            "dump() function to store the object data to the file."
            pickle.dump(self.contactbook, handle)
        print (" Your records saved succesfully in " + filename)
   
    def deserialize(self):
        """ Read records from file """
        filename = input(" Please enter filename to read contact records : ")
        if path.exists(filename):
            with open(filename, 'rb') as handle:
                self.contactbook = pickle.load(handle)
                print (" Your records restored succesfully.")
        else:
            print ("File", filename, "does not exist")

    def remove_contact(self):
        """ remove contact from contactbook"""
        if len(self.contactbook) == 0:
            print (" No data to be deleted ")
        else:
            number = int(input(" Enter number you want to delete : "))
            if number in self.contactbook:
                del self.contactbook[number]
                print (" Your number deleted succesfully ")
            else:
                print(" number not exist ")