"""
Write a program to find a character position in string without using python string function

"""
try:
    name = input("Enter the string : ")
    char = input("\nEnter the character to find its position : ")
    
    def string_position(string : str, character : str):
        "This function return index of given character of string"
        try:
            result = 0
            for i in range(0, len(string)):
                if string[i] == character:
                    result = i
                    break

            if result == 0:
                print("\nNo such character available in string")
            else:
                print("\nCharacter {} is present at index {}".format(character, str(result)))
        except Exception as e:
            print(e)

    string_position(name, char)

except Exception as e:
    print(e)