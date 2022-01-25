###########################################################################
###COP 4045 - Python Programming - Dr. Oge Marques - FAU - Summer 2021 ###
###            Assignment 3: Cryptography app using files              ###
###                    Juan Pablo Idrovo - Z23501186                   ###
###########################################################################


import string

####################### Function for decrypting #####################################################
def decry(message, key):
    print("#######################################################################################\n")
    new_mess = ""
    lett = ""
    size = len(message)
    i = 0

    while i <= size -2:

        lett = message[i]
        if lett.isupper() != False:
            new_mess += chr((ord(lett) - key - 65) % 26 + 65)
        elif lett in string.whitespace + string.punctuation:
            new_mess += lett
        else:
            new_mess += chr((ord(lett) - key - 97) % 26 + 97)
        i+=1

    print(f"OLD message: {message}")
    print(f"New message: {new_mess}\n")

    return new_mess



####################### Function for encrypting #####################################################
def encry(message, key):
    print("#######################################################################################\n")
    new_mess = ""
    lett = ""
    size = len(message)
    i = 0

    while i <= size -1:

        lett = message[i]
        if lett.isupper() != False:
            new_mess += chr((ord(lett) + key - 65) % 26 + 65)
        elif lett in string.whitespace + string.punctuation:
            new_mess += lett
        else:
            new_mess += chr((ord(lett) + key - 97) % 26 + 97)
        i+=1

    print(f"OLD message: {message}")
    print(f"New message: {new_mess}\n")

    return new_mess
    

########################## Main Function ##########################################################


again = "y"

print("\n#######################################################################################\n")
print("\nWelcome to the Caesar Cypher\n")
print('''In this basic app, we are learning string manipulation opening files, closing files, 
reading files, and writing in files. We are going to develop one of the simplest cyphers ever, 
the first one. This one is called  Caesar Cipher, because he used  cryptography to encode  the
messages to his generals. We are going to do something very similar while learning manipulation
of strings, and while learning how to manage input and outputs with text files \n''')
while again == "y" or again == "Y":

    message = input("Please enter the name of the file to READ: \n")
    key_int = int(3)
    operation_str = input("Type E [Encryption] or D [Decryption] \n")
    message = message.strip()
    # Opening the file for reading
    in_file = open(f"{message}.txt", "r")
        

    if operation_str == "e" or operation_str == "E":
        # Opening file for writing
        out_file = open(f"{message}_en.txt", "w")

        for word in in_file:

            new_mess = encry(word, key_int)
            print(new_mess, file = out_file)

        print(f"The file '{message}' was encrypted successfully")

    elif operation_str == "d" or operation_str == "D":
        # Opening the file for writing
        out_file = open(f"{message}_dec.txt", "w")

        for word in in_file:
        
            new_mess = decry(word, key_int)
            print(new_mess, file = out_file)

        print(f"The file '{message}' was decrypted successfully")

    else:
        print("Please choose a correct operation.")

    # Closing the file in_file
    in_file.close()
    # Closing the file out_file
    out_file.close()

    print("#######################################################################################\n")

    print("To try again type y [yes], to quit type n [no]: ")
    again = input(" ")
print("\nThank you for being a part of the Caesar Cypher, have a good day :)\n\n")