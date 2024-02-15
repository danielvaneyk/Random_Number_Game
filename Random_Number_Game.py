import random

# Introduction and information about the game
"""Guess the number game. A bit of fun with guessing a number"""
"""Code by Daniel Van Eyk danielvaneyk@outlook.com"""

def guess_the_number():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    
    while True:
        # Take user input
        guess = int(input("Guess the number (between 1 and 100): "))
        
        # Check the guess
        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print("Congratulations! You guessed the number correctly!")
            break
    
    # Ask if the player wants to play again
    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() == "yes":
        guess_the_number()

# Start the game
guess_the_number()