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
        self.acts[key] = {function:cmd_desc}
        
    def __str__(self):
        menu = str("\n----------------------------------\n")
        for key in self.acts.keys():
            embed = self.acts.get(key)
            for desc in embed.values():
                menu += str(key) + ". " + desc + "\n"
        return menu

    def userchoice(self):
        """ User choices input """
        self.choice = int(input(" Please Enter your choice :- "))

    def run(self):
        """ Working on user choices """
        while True:
            print (self)
            self.userchoice()
            work = self.acts.get(self.choice)
            if work is not None:
                list(work.keys())[0]()
                