#!/user/bin/env python3
'''
Write a program to reverse user defined List Element using recurrsion.

'''
try:
    #Initialize empty list
    list1 = []
    number = int(input("\nEnter range for creating list: "))
    def create_list(a : list):
        "This function used to create list"
        try:
            print("\nOriginal list : ", a)
            for i in range(number):
                new = input("Enter item you want to add in list: ")
                a.append(new)
            print("\nCreated list is : ", a)
        except Exception as e:
            print(e)
        
    create_list(list1)

    def reverse_list(NumList : list, i, j):
        "This funtion return reverse list"
        try:
            if(i < j):
                # Creating a temporary variable
                temp = NumList[i]
                NumList[i] = NumList[j]
                NumList[j] = temp
                # recurrsion
                reverse_list(NumList, i+1, j-1)
   
        except Exception as e:
            print(e)
    print("\nThe Initial number list is = ", list1)

    reverse_list(list1, 0, len(list1)-1)
    print("\nThe Result of a Reverse List =  ", list1)

except Exception as e:
    print(e)