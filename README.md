# Random_Number_Game
The import random statement imports the random module, which is used to generate random numbers.

The guess_the_number() function is defined to encapsulate the game logic.

Inside the guess_the_number() function:

It generates a random integer between 1 and 100 (inclusive) using random.randint(1, 100). This is the number that the player needs to guess.
It enters a loop (while True:) to repeatedly prompt the player for guesses until they guess the correct number.
Inside the loop:
It takes user input using input("Guess the number (between 1 and 100): "), converting it to an integer using int().
It compares the user's guess with the secret number:
If the guess is lower than the secret number, it prints "Too low! Try again.".
If the guess is higher than the secret number, it prints "Too high! Try again.".
If the guess matches the secret number, it prints "Congratulations! You guessed the number correctly!" and breaks out of the loop.
After exiting the loop, it asks the player if they want to play again using input("Do you want to play again? (yes/no): ").
If the player answers "yes", the function calls itself recursively to start a new game.
If the player answers anything other than "yes", the function terminates.
The game starts by calling the guess_the_number() function.

Overall, this program provides a simple and interactive game where the player tries to guess a randomly generated number within a specified range.






