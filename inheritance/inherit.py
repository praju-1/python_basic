'''
Write a program for calculate area of shapes using inheritance
'''

import math

# Creating parent class
class shape:
    # constructor of class
    def __init__(self):
        print("Shape Constructor")

    def get_area(self):
        print(" Area of Shape is : ")


# Creating child class rectangle inherited from shape
class rectangle(shape):
    def __init__(self, length, breadth):
        super().__init__()
        self.length = length
        self.breadth = breadth

    def get_length(self):
        # get the length of rectangle
        return self.length

    def get_breadth(self):
        # get the breadth of rectangle
        return self.breadth

    def get_area(self):
        # calculate area of rectangle
        return self.length * self.breadth

# Creating child class circle inherited from shape
class circle(shape):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius

    def get_radius(self):
        # return radius of circle
        return self.radius

    def get_area(self):
        # calculate area of circle
        return math.pi * self.radius **2

if __name__ == "__main__":
    rect = rectangle(10, 20)
    print(" Area of rectangle is: ", rect.get_area())

    cir = circle(5)
    print(" Area of circle is :", cir.get_area())


