'''
Write a program for polymorohism with relations.
'''

# Defining parent class vehicle
class Vehicle:
    # Methods of class
    def info(self):
        print(" There are many types of vehicles ")

    def feature(self):
        print(" Vehicles are use for travelling \n ")

# Defining child class
class Two_wheeler(Vehicle):
    def info(self):
        print(" A two-wheeler is a vehicle that runs on two wheels.")

    def feature(self):
        print(" Two wheeler has a integrated braking system. \n Also Telescopic Front Suspension \n ")

# Defining another child class
class Four_wheeler(Vehicle):
    def info(self):
        print(" A four-wheeler is a vehicle that runs on Four wheels. ")

    def feature(self):
        print(" Four wheeler has Antilock Brakes. \n Also Electronic Stability Control")
#
# Entrypoint of program
#
if __name__ == "__main__":
    # Object of class Vehicle
    obj_veh = Vehicle()
    # Object of class Two_wheeler
    obj_tw = Two_wheeler()
    # Object of class Four_wheeler
    obj_fw = Four_wheeler()

    # Calling methods of class
    obj_veh.info()
    obj_veh.feature()

    obj_tw.info()
    obj_tw.feature()

    obj_fw.info()
    obj_fw.feature()