'''Write a program to create threads'''

from threading import Thread

# No of thread to be created
number_of_threads = 10

# Creating generator here
def even_numbers():
    """ This function will return even number with its thread"""
    for number in range(50):
        number % 2 == 0


if __name__ == "__main__":

    # creating threads using generator Expression
    threads =  (Thread(target = even_numbers) for t in range(number_of_threads))

    # start threads
    for t in threads:
        t.start()

    # join threads
    for t in threads:
        t.join()

    # printing the threads
    print("Threads are : ","\n", threads)

    print(" End main ")