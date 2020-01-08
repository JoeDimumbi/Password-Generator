'''

Author = @JoeDimumbi
Date = 2020/01/04 
This is my first Python script to generate a random password by asking the user what kind of password to enter

'''
#importing library that will be useful for generating random password

import random       #Gives me a library of argument I can use to link, generate and do more with strings
import string       #Gives me access to a varieties of strings(alphabets, symbols and numbers)
import os           #Haven't used it in depth yet but I'm using it to keep the terminal open while the program is running


#From the string Library

#string.ascii_letters 		:Incorporate Capitals and Small letters
#string.punctuation       	:All symbols or punctuations
#string.digits            	:All the numbers from 0 to 9

print("How long do you want your password to be? Type a number between 6 to 12 \n")
pass_length = int(input("Enter length of the password\n"))


print("Your password can either be: \n")

print("\tLetters only:  type letters \n")
print("\tNumbers only:  type numbers \n")
print("\tLetters with symbols and numbers:  type medium1 \n")
print("\tLetters with symbols and letters:  type medium2 \n")
print("\tLetters with symbols and numbers and letters:  type complex \n\n")

pass_type = input("What kind of password do you want to generate? \n")


while pass_length > 6:

    if pass_type == "letters":

        pass_char = string.ascii_letters 														
        gen_pass =  "".join(random.choice(pass_char) for num in range(random.randint(6, 12)))
        
        if pass_length == len(gen_pass):

            print ("Your password is: " +gen_pass)
            break

    elif pass_type == "numbers":

        pass_char = string.digits 																
        gen_pass =  "".join(random.choice(pass_char) for num in range(random.randint(6, 12)))
        
        if pass_length == len(gen_pass):
            
            print ("Your password is: " +gen_pass)
            break
    elif pass_type == "medium1":

        pass_char = string.punctuation +  string.digits
        gen_pass =  "".join(random.choice(pass_char) for num in range(random.randint(8, 12)))

        if pass_length == len(gen_pass):

            print ("Your password is: " +gen_pass)
            break
    elif pass_type == "medium2":

        pass_char = string.punctuation +  string.ascii_letters
        gen_pass =  "".join(random.choice(pass_char) for num in range(random.randint(8, 12)))
        
        if pass_length == len(gen_pass):

            print ("Your password is: " +gen_pass)
            break
    elif pass_type == "complex":

        pass_char = string.punctuation +  string.ascii_letters +  string.digits
        gen_pass =  "".join(random.choice(pass_char) for num in range(random.randint(8, 12)))
        
        if pass_length == len(gen_pass):
        
            print ("Your password is: " +gen_pass)
            break
    else:

        print(f"Your selection {pass_type} is not valid: ")
    

def exit_func():

    exit_input = input("Are you sure you want to exit? yes or no? \n")

    if exit_input == "yes":

        exit()

    elif exit_input == "no":

        pass

    else: 

        exit_func()


os.system("pause")
