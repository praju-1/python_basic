#!/usr/bin/env python3
""" Python program to check whether given string is isogram using Hashmap """

"""
Defination of Isogram string : A word or phrase in which each letter occurs the same number of times.
"""

"""
Hashmap : 
In this, the count of characters of the string is stored in the hashmap, 
and wherever it is found to be greater than 1 for any char, return false else return true at the end
"""

try:
    string = str(input(" Enter the string : "))
    string2 = str(input(" Enter another string : "))
    def check_isogram(string): 
        "This function check string for isogram"
        try:
            length = len(string) 
            mapHash = [0] * 26 
        
            """ checking the length of string""" 
            # loop to store count of chars
            # and check if it is greater than 1 
            for i in range(length): 
                #Declare a hashmap to store the count of the characters of the string 
                mapHash[ord(string[i]) - ord('a')] += 1  
                """if count > 1, return false"""  
                if (mapHash[ord(string[i]) - ord('a')] > 1):
                    return False  
            return True  
        
        except Exception as e:
            print(e)
                              
    """checking str as isogram"""  
    if (check_isogram(string)): 
        print(" Given string1 is isogram ")  
    else: 
        print("\nGiven string1 is not isogram ")  
            
    """checking str2 as isogram"""  
    if (check_isogram(string2)) : 
        print("\nGiven string2 is isogram ") 
    else:  
        print("\nGiven string2 is not isogram ")
       
except Exception as e:
    print(e)