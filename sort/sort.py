"""
Write a program to sort random no.list without using sort function

"""
import random
try:
    i = int(input("Enter range for random list : "))
    def create_list(limit : int):
        "This function return list of random interger"
        try:
            #It return a list with a randomly selection specified number of items from a sequnce
            return random.sample(range(1,50), limit)
        except Exception as e:
            print(e)


    def swap_num(Numlist : list, a : int, b : int):
        "This function swap number between two number"
        try:
            #here tmp we create temporary variable to store value
            tmp = Numlist[a]
            Numlist[a] = Numlist[b]
            Numlist[b] = tmp
        except Exception as e:
            print(e)

    def sort(Numlist : list):
        "This function return sorted list"
        try:
            for i in range(0, len(Numlist)-1):
                for j in range(i + 1, len(Numlist)):
                    if Numlist[i] > Numlist[j]:
                        swap_num(Numlist, j, i)
                        print ("\nSwapping ", i, " and ", j, "list now: ", Numlist)
            return Numlist
        except Exception as e:
            print(e)

    if __name__ == "__main__":
        presort = create_list(i)
        print ("\nRandom list is : ", presort)

        sorted_list = sort(presort)
        print ("\nSorted list is : ", sorted_list)
except Exception as e:
    print(e)
