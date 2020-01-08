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

print("How long do you want your password to be? Type a number between 6 to 12 \n")
pass_length = int(input("Enter length of the password\n"))

while pass_length > 6:                                                  #Making sure that the password entered is greater than 6

    print("Your password can either be: \n")

    print("\tLetters only:  type letters \n")
    print("\tNumbers only:  type numbers \n")
    print("\tLetters with symbols and numbers:  type medium1 \n")
    print("\tLetters with symbols and letters:  type medium2 \n")
    print("\tLetters with symbols and numbers and letters:  type complex \n\n")

    pass_type = (input("What kind of password do you want to generate? \n")).lower()


    if pass_type == "letters":                                          #Condition to generate password with letters only

        pass_char = string.ascii_letters 														
        gen_pass =  "".join(random.choice(pass_char) for num in range(random.randint(6, 12)))
        
        if pass_length == len(gen_pass):

            print ("Your password is: " +gen_pass)
            print ("Thank you for using Password Generator V 1.0.0")
            break

    elif pass_type == "numbers":                                        #Condition to generate password with numbers only

        pass_char = string.digits 																
        gen_pass =  "".join(random.choice(pass_char) for num in range(random.randint(6, 12)))
        
        if pass_length == len(gen_pass):
            
            print ("Your password is: " +gen_pass)
            print ("Thank you for using Password Generator V 1.0.0")
            break
    elif pass_type == "medium1":                                        #Condition to generate password with symbols and digits only

        pass_char = string.punctuation +  string.digits
        gen_pass =  "".join(random.choice(pass_char) for num in range(random.randint(6, 12)))

        if pass_length == len(gen_pass):

            print ("Your password is: " +gen_pass)
            print ("Thank you for using Password Generator V 1.0.0")
            break
    elif pass_type == "medium2":                                        #Condition to generate password with symbols and letters only

        pass_char = string.punctuation +  string.ascii_letters
        gen_pass =  "".join(random.choice(pass_char) for num in range(random.randint(6, 12)))
        
        if pass_length == len(gen_pass):

            print ("Your password is: " +gen_pass)
            print ("Thank you for using Password Generator V 1.0.0")
            break
    elif pass_type == "complex":                                        #Condition to generate password with symbols, digits and letters only

        pass_char = string.punctuation +  string.ascii_letters +  string.digits
        gen_pass =  "".join(random.choice(pass_char) for num in range(random.randint(6, 12)))
        
        if pass_length == len(gen_pass):
        
            print ("Your password is: \n" +gen_pass)
            print ("Thank you for using Password Generator V 1.0.0\n")
            break
    else:                                                               #Invalid input from the user

        print(f"Your selection {pass_type} is not valid: ")             #If user input is not valid, return to beginning or exit
        pass_type_error = input("\nWould you like to start over? Y/N \n").lower() #User input decision to continue or exit                  

        if pass_type_error == "y" or "yes":

            #goto beginning
            break
        elif pass_type_error == "n" or "no":

            sys.exit()
            break
        else:
            print("You have entered an invalid value")
            sys.exit()
            break

else:

        print(f"The value entered {pass_type}, is not valid: \n")  
        print("Next time enter a value greater than 6 \n")   

def exit_func():                                                        #Exit function not used yet

    exit_input = input("Are you sure you want to exit? yes or no? \n")

    if exit_input == "yes":

        sys.exit()

    elif exit_input == "no":

        pass

    else: 

        exit_func()


os.system("pause")                                                              #Keep the terminal open
