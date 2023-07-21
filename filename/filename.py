"""
Write a program to print all filenames from given folder

"""
import os, argparse

def file_list(dirname):
    ## check if input dir exists

    filelist = os.listdir(dirname)
    return filelist

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--list", "-l", help="Please provide directory name.")
    args = parser.parse_args()

    if args.list:
        files = file_list(args.list)
        for file in files:
            print (">> ", file)
    else:
        print (parser.print_help())

