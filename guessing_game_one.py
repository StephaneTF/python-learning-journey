import random

# Random number between 1 and 9 (inclusive)
random_number = random.randint(1, 9)
# Track number of guesses
guess_count = 0

# Welcome message
print("*****Welcome To Guessing Game One*****.")
print("I'm thinking of a number between 1 and 9. Type 'exit' or quit.")

# Main game loop
# Runs an infinite loop until the user types "exit"
while True:
    # Get user number
    user_input = input("Enter your guess (1-9) or 'exit': ").lower()

    # Check user_input wants to exit
    if user_input == "exit":
        print(f"Game over! you made {guess_count} guesses.")
        print(f"The number was {random_number}.")
        break

    # Validate input is a number

    # isdigit(): a sting method that checks
    # if all characters in a string are digits(0-9) it returns
    # True if every character is a digit (eg, "123")
    # False if any character isn't a digit (eg, "12a","-1","abc")

    if not user_input.isdigit():
        print("Please enter a number between 1 and 9 or 'exit'.")
        continue
    
    # Convert input to integer and check range
    guess = int(user_input)
    if guess < 1 or guess > 9:
        print("Please enter a number between 1 and 9.")
        continue
    # Increment guess counter for each valid guess
    guess_count += 1
    
    # Compare guess to random number 
    if guess == random_number:
        print(f"You guessed exactly right! You got it in {guess_count} guesses!")
        print("Starting a new game...")

        # Pick a new number
        random_number = random.randint(1, 9)

        # Reset guess counter
        guess_count = 0 

    elif guess > random_number:
        print("You guessed too high! Try again.")
    else:
        print("You guessed too low! Try again.")

    # Ask to play again
    play_again = input("Play again? (yes/no): ")
    if play_again != "yes":
        print("Thanks for playing!")
        break
