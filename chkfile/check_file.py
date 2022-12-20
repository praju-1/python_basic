"""
Write  a program to check whether file or directory exist or not at a given location

"""

# Importing os module
import os.path
from os import path
from os.path import exists

#path for the files
location = 'F:\Data_science\Gitworkplace\python_basic\chkfile\demo.txt'
location1 = 'F:\Data_science\Gitworkplace\python_basic\chkfile'

try:
    def check_file():
        "This function return boolean result for file is exist or not"
        try:

            #It check given file is exist or not
            print("\nIs given file exist ? : " + str(path.exists(location)))
            
            #It check given path contain directory or not
            print("\nIs directory exists ? : " + str(path.isdir(location1)))
            
            #Checking for file existence
            print("\nDoes given location contain a file ?  : " + str(path.isfile(location)))

            #Checking for file existence
            print("\nDoes given location contain a file ?  : " + str(path.isfile(location1)))



        except Exception as e:
            print(e)
    
    check_file()

except Exception as e:
    print(e)
