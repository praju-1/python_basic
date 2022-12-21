'''
Write program to print information of Operating system, Hardware and Application.
'''

#Importing module 
import psutil                   # access system details and process utilities
import platform                 # access information of operating system
import os, sys                  # provides functions for interacting with the operating system
from datetime import datetime   # supplies classes for manipulating dates and times
import threading                # allows you to create and manage new threads


# specifies length for title 
LINE_SZ = 40
try:
    def pretty_print(frame_char, title="", size=LINE_SZ):
        """This function help to print output in better format"""
        try:
            #checking for blank space in title
            if  frame_char.isspace() and title != "":
                print(frame_char * size + title)
                return

            if title != "":
                size = size - int(len(title) / 2) - 2
                print(frame_char * size + " " + title + " " + frame_char * size)
                return

            size *= 2
            print(frame_char * size + "\n")

        except Exception as e:
            print(e)

    def os_info():
        "This function return all information about operation system using platform module"
        try:
            pretty_print("*",  "OS Information")
            pretty_print(" ", "Operating system : " + platform.system(), 2)
            pretty_print(" ", "Operating system release : " + platform.release(), 2)
            pretty_print(" ", "Platform : " + platform.system(), 2)
            pretty_print(" ", "Machine Type : " + platform.machine(), 2)
            pretty_print(" ", "Processor Type : " + platform.processor(), 2)
            pretty_print(" ", "Platform Type : " + platform.platform(), 2)
            pretty_print("*")

        except Exception as e:
            print(e)
    os_info()

    def hardware_info():
        "This function return information about CPU using psutil module"
        try:
            # let's print CPU information
            pretty_print("*", "Hardware Information")
            # number of cores
            print("Physical cores:", psutil.cpu_count(logical=False))
            print("Total cores:", psutil.cpu_count(logical=True))
            # CPU frequencies
            cpufreq = psutil.cpu_freq()
            print(f"Max Frequency: {cpufreq.max:.2f}Mhz")
            print(f"Min Frequency: {cpufreq.min:.2f}Mhz")
            print(f"Current Frequency: {cpufreq.current:.2f}Mhz")
            # CPU usage
            print("CPU Usage Per Core:")
            #iterate through cpu
            for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
                print(f"Core {i}: {percentage}%")
            print(f"Total CPU Usage: {psutil.cpu_percent()}%")
            pretty_print("*")

        except Exception as e:
            print(e)

    hardware_info()
    
    def application_info():
        "This function return information about application we used using os module"
        try:
            pretty_print("*", "Application information")
            pyversion = str(sys.version)
            pyversion = ''.join(pyversion.split("\n"))
            pretty_print(" ", "Python Version : " + pyversion, 1)
            pretty_print(" ", "Working Directory : " + os.getcwd(), 1)
            pretty_print(" ", "Process Id : " + str(os.getpid()), 1)

            # Print local time
            time = datetime.now().time()
            pretty_print(" ", "Current Local time : " + str(time), 1)
            
            # Print the current date and time in UTC
            pretty_print(" ", "Current UTC time : " + str(datetime.utcnow()), 1)

            # Print no of thread in application
            pretty_print(" ", "Active threads : " + str(threading.active_count()), 1)
            pretty_print("*")

        except Exception as e:
            print(e)
    
    application_info()

except Exception as e:
    print(e)