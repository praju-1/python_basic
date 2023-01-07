#!/usr/bin/env python3
""" defining class for user actions """
class Actions: 
    """
    A class to represent a Actions of user
    .....
    Methods
    -------
    register():
        Register the users keys for cmd_desc
    userchoice():
        Taking input from user for choices
    run():
        Run program depends on choice of user
    """
    def __init__(self):
        """
        Constructs all the necessary attributes for the contactbook object
        """
        self.acts = {}
        self.choice = 0
        
    def register(self, key, function, cmd_desc):
        try:
            self.acts[key] = {function:cmd_desc}
        except Exception as e:
            print(e)

    def __str__(self):
        "This method returns the string representation of the object."
        try:
            menu = str("\n----------------------------------\n")
            
            for key in self.acts.keys():
                embed = self.acts.get(key)
                for desc in embed.values():
                    menu += str(key) + ". " + desc + "\n"
            return menu
        except Exception as e:
            print(e)

    def userchoice(self):
        """ User choices input """
        try:
            self.choice = int(input(" Please Enter your choice :- "))
        except Exception as e:
            print(e)

    def run(self):
        """ Working on user choices """
        try:
            while True:
                print (self)
                self.userchoice()
                work = self.acts.get(self.choice)
                if work is not None:
                    list(work.keys())[0]()
        except Exception as e:
            print(e)           