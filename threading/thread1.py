'''
Write a program to create threads using lock
'''
import threading

limit       = 10
signal_sem  = threading.Semaphore(0)
locker_sem  = threading.Semaphore(1)

# Defining function for even number
def even_numbers():
    for number in range(limit):
        if(number % 2) == 0:
            # Applying locker lock
            locker_sem.acquire()
            print(" Even_Thread id is {}  : even number {}".format(threading.get_native_id(), number))
            # Unlock signal lock
            signal_sem.release()

# Defining function for odd number
def odd_numbers():
    for number in range(limit):
        if(number % 2) != 0:
            # Applying signal lock
            signal_sem.acquire()
            print(" Odd_Thread  id is {}  : odd number {}".format(threading.get_native_id(), number))
            # Unlock locker lock
            locker_sem.release()
#
# Entrypoint of program
#
if __name__ == "__main__":
    # Creating threads
    even_thread = threading.Thread(target=even_numbers)
    odd_thread = threading.Thread(target=odd_numbers)

    # Start thread
    even_thread.start()
    odd_thread.start()

    # join thread
    even_thread.join()
    odd_thread.join()