'''
Write a program for polymorphism with objects.
'''

# Defining class for fiction book
class The_Alchemist():
    def type(self):
        print(" The Alchemist is a fiction Book ")

    def author(self):
        print(" Author of the book is : Paulo Coelho ")

# Defining class for Non-fiction book
class Wise_And_Otherwise():
    def type(self):
        print("\n Wise And Otherwise book is Non-Fiction book ")

    def author(self):
        print(" Author of book is : Sudha Murty ")

# Creating function allowing for polymorphism
def poly(obj):
    # calling methods of class
    obj.type()
    obj.author()

if __name__ == "__main__":
    # Creating instantiation of both class
    obj_fiction = The_Alchemist()
    obj_nonfiction = Wise_And_Otherwise()

    poly(obj_fiction)
    poly(obj_nonfiction)
