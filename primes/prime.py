"""
Compute prime no. in user define range

INPUT : Enter the starting and ending number (range)
OUTPUT : return the prime numbers between the range given by user

"""
try:
    #It will take input from user
    a = int(input("Enter the number from you want prime number : "))
    b = int(input("Enter the number upto you want prime number : "))
            
    def prime_number(num1 : int, num2 : int):
        " This function return the total prime number between given range"
        try:
            count = 0
            for element in range(num1, num2):
                #This check condition for prime number
                if element % 2 == 0:
                    print ("The Prime number is  : ", element)
                    count += 1
            print("\nThe total prime numbers between", num1, "and", num2, "is :", count)

        except Exception as e:
            print(e)

    prime_number(a, b)
except Exception as e:
            print(e)

