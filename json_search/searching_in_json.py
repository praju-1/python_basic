#!/usr/bin/python3
'''
Write a program for parse json file for searching user define value.

'''

# to run enter file name and key from json file


import json
import sys, getopt

#
# printing usage
#
def usage(argv):
    print(argv[0], "-h: print this help.")
    print(argv[0], "-f <json file> -s search key")
    return
#
# searching for user define value(specific key)
#
def search(json_schema, json_key):
    # Checking type of the json file
    if type(json_schema) is dict:
        for key in json_schema:
            if type(json_schema[key]) in (list, dict):
                search(json_schema[key], json_key)
            elif key == json_key:
                print (json_schema[key])
    elif type(json_schema) is list:
        for item in json_schema:
            if type(item) in (list, dict):
                search(item, json_key)

#
# Validate json file
#
def validate_json(filename):
    try:
        with open(filename, "r") as f:
            json_data = f.read()
    # output error
    except ValueError as e:
        print("Error in opening file : ", e)
        return None

    try:
        json_schema = json.loads(json_data)
    except ValueError as e:
        print("Invalid json : ", e)
        return None

    return json_schema
#
# using command line argument
#
def main(argv):
    filename=""
    json_key=""

    # parsing argument
    opts, args = getopt.getopt(argv[1:], "f:s:h")
    if len(opts) == 0:
        usage(argv)
        return

    # cheking each argument
    for opt, args in opts:
        if opt == "-f":
            filename = args
        if opt == "-s":
            json_key = args
        if opt == "-h":
            usage(argv)
            return

    if filename != '' and json_key != '':
        schema = validate_json(filename)
        if schema != None:
            search(schema, json_key)
    else:
        usage(argv)

#
# Entrypoint of program
#
if __name__ == "__main__":
    main(sys.argv)

