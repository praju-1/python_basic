'''
Write a program for polymorphism with class method

'''

# Definition of the class start here
class employee1:
    # Defining constructor
    def __init__(self, name, age, designation):
        self.name = name
        self.age = age
        self.designation = designation

    #defining class method
    def info(self):
        print(f" My name is {self.name}. I am {self.age} years old. My designation is {self.designation} ")

class employee2:
    def __init__(self, name, age, designation):
        self.name = name
        self.age = age
        self.designation = designation

    def info(self):
        print(f" My name is {self.name}. I am {self.age} years old. my designation is {self.designation} ")


if __name__ == "__main__":
    # Create an object of class
    person1 = employee1("John", 22, "Software Engineer")
    # Create another object of the class
    person2 = employee2("Kiara", 25, "Senior software Engineer")

    # Iterate through a touple of objects
    # Using common variable
    for person in (person1, person2):
        person.info()