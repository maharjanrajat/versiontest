import random

def guess(x):
    random_number = random.randint(1,x)
    
    guess = 0
    
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        
        if guess < random_number:
            print("Sorry, Too low! Guess Again.")
        elif guess > random_number:
            print("Sorry, Too high! Guess Again.")
        
    print("Congratulation!! You have guessed it correct.")
        
guess(10)    