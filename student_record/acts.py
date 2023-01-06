#!/usr/bin/env python3
'''
Action provides -
1. register - register the description.
2. userchoice - get user choice input.
'''
class Actions:

    def __init__(self):
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
        self.choice=int(input(" Please Enter your choice :- "))

    def run(self):
        while True:
            # print options / menu
            print (self)
            self.userchoice()
            # call choiced act
            work = self.acts.get(self.choice)
            if work != None:
                list(work.keys())[0]()