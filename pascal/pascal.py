#!/usr/bin/env python3
'''
Write a program to print Pascal triangle.

Pascal triangle : Pascal’s triangle, in algebra, a triangular arrangement of numbers that gives 
the coefficients in the expansion of any binomial expression

'''
try: 
    n = int(input(" Enter the number of rows : "))
    def pascal_triangle(limit : int):
        "This function print pascal triangle"
        try:
            for line in range(1, limit):
                first_val = 1
                print("\n")
                #Printing the spaces before 1st char
                print(" " * (limit - line), end='')

                #Iterate through every line
                for value in range(1 , line + 1):
                    #first value in line is always 1
                    print(first_val,  " ", end='')
                    first_val = int((first_val * (line - value) / value))
            print("\n")
        except Exception as e:
            print(e)

    pascal_triangle(n + 1)
except Exception as e:
    print(e)