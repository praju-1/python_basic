#!usr/bin/env python3
"""
Program for checking given string is symmetry or not, with illustration of exec()

The exec() method executes a dynamically created program, which is either a string or a code object.

"""
word = input(" Enter the string : ")
def executable_code():
    "This function execute the function"
    string = """
def string_symmetry(word):
    "This function check for symmetric string"
    n = len(word)
    flag = 0

    # Check if the string's length is odd or even
    if n%2:
        mid = n//2 +1
    else:
        mid = n//2

    start1 = 0
    start2 = mid

    while(start1 < mid and start2 < n):

        if (word[start1]== word[start2]):
            start1 = start1 + 1
            start2 = start2 + 1
        else:
            flag = 1
            break
        # Checking the flag variable to
    # check if the string is symmetrical
    # or not
    if flag == 0:
        print(" The entered string is symmetrical ")
    else:
        print(" The entered string is not symmetrical ")
print(string_symmetry(word))
    """
    exec(string)
executable_code()