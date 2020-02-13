'''
Author = @JoeDimumbi
Date = 2020/01/04 
This is my first Python script to generate a random password by asking the user what kind of password to enter
'''
#importing library that will be useful for generating random password

import random       #Gives me a library of argument I can use to link, generate and do more with strings
import string       #Gives me access to a varieties of strings(alphabets, symbols and numbers)
import os           #Haven't used it in depth yet but I'm using it to keep the terminal open while the program is running
import sys

#From the string Library

#string.ascii_letters 		:Incorporate Capitals and Small letters
#string.punctuation       	:All symbols or punctuations
#string.digits            	:All the numbers from 0 to 9

#-------------------------------------------------------------------------------------------------------------------------------

def main():                                                                                    #Main function where 
    
    if pass_leng < 6:
        error()
        exit_func()
    elif 6 <= pass_leng <= 12:
        password_type()
        save_in_file()
        exit_func()
    elif pass_leng > 12:
        error()
        exit_func() 

#-------------------------------------------------------------------------------------------------------------------------------

def error():
    print("\nYour input is less than 6 or greater than 12!!!\n")

def password_type():

    if pass_type == 1:

        pass_char = string.ascii_letters 
        print("\nYour password is: ")
        print(''.join(random.choice(pass_char) for i in range (pass_leng)))

    elif pass_type == 2:

        pass_char = string.digits
        print("\nYour password is: ")
        print(''.join(random.choice(pass_char) for i in range (pass_leng)))
        
    elif pass_type == 3:

        pass_char = string.punctuation +  string.digits
        print("\nYour password is: ")
        print(''.join(random.choice(pass_char) for i in range (pass_leng)))

    elif pass_type == 4:

        pass_char = string.punctuation +  string.ascii_letters
        print("\nYour password is: ")
        print(''.join(random.choice(pass_char) for i in range (pass_leng)))
        
    elif pass_type == 5:

        pass_char = string.ascii_letters +  string.digits
        print("\nYour password is: ")
        print(''.join(random.choice(pass_char) for i in range (pass_leng)))
    
    elif pass_type == 6:

        pass_char = string.punctuation +  string.ascii_letters +  string.digits
        print("\nYour password is: ")
        print(''.join(random.choice(pass_char) for i in range (pass_leng)))
    
    else:

        print(f"Your selection {pass_type} is not valid: ")
        exit_func()

def save_in_file():                                                                                 #Function to save password in a file
    prompt_output_file = input("Do you want to save this password in a .txt file? y or n? \n")

    if prompt_output_file == "y":
        f = open("password_output.txt", "a")
        print("Trying to print the password in this file!", file=f)
        f.close()

    elif prompt_output_file == "n":
            exit_func()

def exit_func():                                                                                   #Exit function to allow the user to leave the code

    exit_input = input("\nDo you want to exit? y or n? \n")

    if exit_input == "y":
        print("\nThank you for using my password generator\n")
        exit()

    elif exit_input == "n":
        pass
    else: 
        print("\nERROR!\n")
        exit_func()
#-------------------------------------------------------------------------------------------------------------------------------

pass_leng = int(input("Enter the length of your desired password? Type a number between 6 to 12 \n"))       #Prompting the user to input lenght and type of password

print("\nYour password can either be: \n")

print("\tLetters only:  type 1 \n")
print("\tNumbers only:  type 2 \n")
print("\tLetters with symbols and numbers:  type 3 \n")
print("\tLetters with symbols and letters:  type 4 \n")
print("\tLetters with numbers and letters:  type 5 \n\n")
print("\tLetters with symbols and numbers and letters:  type 6 \n\n")

pass_type = int(input("\nnter the type of password you want to generate \n"))
main()

#-------------------------------------------------------------------------------------------------------------------------------    
