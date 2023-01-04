#!/usr/bin/env python3
""" display the output format """
class Contact:
    """
    A class to represent a contact
    ...
    Attributes
    ----------
    name : str
        name for contact details
    number : int
        number for contact details
    city : str
        city for contact details
    email : str
        email for contact details

    Methods
    -------
    __str__():
        display the string representation of the object 
    """
    def __init__(self, name, number, city, email):
        """
        Constructs all the necessary attributes for the contactbook object
        """
        self.name = name
        self.number = number
        self.email = email
        self.city = city

    def __str__(self):
        """ Display record format """
        return "\n----------------------------------------\n" + \
            "\nName     : " + self.name + \
            "\nNumber   : " + str(self.number) + \
            "\nCity     : " + self.city + \
            "\nEmail    : " + self.email   