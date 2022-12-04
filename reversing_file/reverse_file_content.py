"""
Write a program to print file content in reverse order

"""
try:
    content = input("Enter content for file you want to write and reverse : ")
    file = input("Enter filename you want to open : ")

    def write_to_file(filename, data):
        "This function open file for writing"
        try:
            "File open in write mode"
            file = open(filename,"w")
            file.write(data)
            file.close()
        except Exception as e:
            print(e)

    def filereverse(filename):
        "This function reverse the content of the file."
        try:
            rev_content = []
            with open(filename) as file:
                data = file.readlines()
                r = reversed(data)

            for line in r:
                rev_content.append(line[::-1])

            return rev_content
        except Exception as e:
            print(e)

        
    write_to_file(file, content)
    print("\nOrignal data from file  is : \n", content)
    file_content = filereverse(file)

    print ("\nReverse content of file: \n")
    for line in file_content:
        print (line)
 
except Exception as e:
    print(e)