# Guessing Game_2602118490_Clarissa Audrey Fabiola Kusnadi

import random
randomint = random.randint(1,100) 
input_number = None

input_name = input("Welcome to the guessing game! What is your name?: ")

while input_number != randomint:
    input_number = int(input("Hello " + input_name + "," + " guess a number from 1-100: "))
    
    if input_number > randomint:
        print("Your guess is too high")
    
    elif input_number < randomint:
        print("Your guess is too low")
    
    else:
        print("Good job! You guessed it correctly.")

