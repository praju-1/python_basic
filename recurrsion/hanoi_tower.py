#!usr/bin/python3
'''
Write a program to solve Hanoi Tower using recurssion.

'''
try:
    # user input for number of disk
    n = int(input(" Enter the number of disk : "))
    def hanoi_tower(n , source, destination, auxiliary):
        try:
            # move n disk from source to destination
            if n == 1:
                print(" Disk 1 move from source", source, "to destination", destination)
                return
            # move n-1 disk from source to auxiliary
            hanoi_tower(n-1, source, auxiliary, destination)

            print(" Disk", n, "move from source", source, "to destination", destination)
            
            #move n-1 disk from auxiliary to destination
            hanoi_tower(n-1, auxiliary, destination, source)
 
        except Exception as e:
            print(e)   
    # A, B, C are source, destination and auxiliary
    hanoi_tower(n, 'A', 'B', 'C')

except Exception as e:
    print(e)