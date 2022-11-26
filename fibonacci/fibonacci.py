'''
Write a program to check given number is Fibonacci number ?

Defination of fibonacci number : Fibonacci number is obtained by adding the two preceding numbers
from fibonacci sequence.

'''

import math

try:
    def perfect_square(x):
        "This function return the perfect square of the given number"
        s = int(math.sqrt(x))
        return s*s == x

    def fibonacci(n):
        "This functionn check the fibonacci sequence."
        if((perfect_square(5*n*n* +4)) or (perfect_square(5*n*n - 4))):
            return True
        return False

    if __name__ == "__main__":
        n = int(input("Enter the number : "))

        if (fibonacci(n) == True):
            print (n, "is a Fibonacci Number")
        else:
            print (n, "is not a Fibonacci Number")
except Exception as e:
    print(e)
    