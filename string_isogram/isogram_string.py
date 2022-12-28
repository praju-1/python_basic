"""
 Python program to check if a word is isogram or not

"""
try: 
    string = input("Enter work to check : ")
    def is_isogram(word):
        "This function return string is isogram or not"
        try:
            # Convert the word or sentence in lower case letters.
            our_word = word.lower()
        
            # Make an empty list to append unique letters
            unique_letter = []

            #iterate through each letter of word
            for letter in our_word:
        
                # If letter is an alphabet then only check
                if letter.isalpha():
                    if letter in  unique_letter:
                        return False
                    unique_letter.append(letter)
        
            return True
        except Exception as e:
    
            print(e)
    # Function call
    result = is_isogram(string)
    if result:
        print("Given word is isogram ")
    else:
        print("Given word is not isogram ")

except Exception as e:
    print(e)