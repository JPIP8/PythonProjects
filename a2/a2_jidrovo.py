###########################################################################
###COP 4045 - Python Programming - Dr. Oge Marques - FAU - Summer 2021 ###
###            Assignment 2: Basic cryptography app                    ###
###                    Juan Pablo Idrovo - Z23501186                   ###
###########################################################################


# Since this is an introductory course, we are studying from the begining. We now 
# are in strings and how to manipulate strings. We are going to develop one of the
# simplest cyphers ever, the first one. This one is called Caesar Cipher, because 
# he used cryptography to encode the messages to his generals. We are going to do 
# something very similar while learning manipulation of strings.
#import abc
import string

# Function for decrypting #####################################################
def decry(message, key):
    print("############################################################\n")
    new_mess = ""
    lett = ""
    key = int(key)
    size = len(message)
    i = 0

    while i <= size -1:

        lett = message[i]
        if lett.isupper() != False:
            new_mess += chr((ord(lett) - key - 65) % 26 + 65)
        else:
            new_mess += chr((ord(lett) - key - 97) % 26 + 97)
        i+=1

    print(f"OLD message: {message}")
    print(f"New message: {new_mess}")



# Function for encrypting #####################################################
def encry(message, key):
    print("############################################################\n")
    new_mess = ""
    lett = ""
    key = int(key)
    size = len(message)
    i = 0

    while i <= size -1:

        lett = message[i]
        if lett.isupper() != False:
            new_mess += chr((ord(lett) + key - 65) % 26 + 65)
        else:
            new_mess += chr((ord(lett) + key - 97) % 26 + 97)
        i+=1

    print(f"OLD message: {message}")
    print(f"New message: {new_mess}")
    

# Main Function ##########################################################

again = "y"

print("\n\nWelcome to the Caesar Cypher\n\n")

print("Since this is an introductory course, we are studying from the begining. We now are in strings and how to manipulate strings.")
print("We are going to develop one of the simplest cyphers ever, the first one. This one is called Caesar Cipher,")
print("because he used cryptography to encode the messages to his generals. We are going to do something very similar while learning manipulation of strings. \n")

while again == "y" or again == "Y":

    print("Type with No space - No punctuation symbols - No other characters\n")
    message = input("Please enter a phrase: \n")
    key_int = int(input("Enter KEY: \n"))
    operation_str = input("Type E [Encryption] or D [Decryption] \n")

    if operation_str == "e" or operation_str == "E":
        encry(message, key_int)
    elif operation_str == "d" or operation_str == "D":
        decry(message, key_int)
    else:
        print("Incorrect option :(")

    print("############################################################\n")

    print("To try again type y [yes], to quit type n [no]: ")
    again = input(" ")