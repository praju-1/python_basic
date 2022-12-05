'''
Write a program to check whether given year is leap year or not

Defination of Leap year : a year that contains 366 days, with February 29 as an 
additional day: occurring in years whose last two digits are evenly divisible by four, 
except for centenary years not divisible by 400.

Input : Enter year to check
'''
try:
    year = int(input("Enter the year : "))
    def check_leap_year(year : int):
        try :
            print("\nThe year is : ", year)
            if (((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0)):
                return True
            else:
                return False
        except Exception as e:
            print(e)
    
    leap_year = check_leap_year(year)
    if(leap_year):
        print("\nGiven year is Leap year. ")
    else:
        print("\nGiven year is not Leap year.")
except Exception as e:
            print(e)