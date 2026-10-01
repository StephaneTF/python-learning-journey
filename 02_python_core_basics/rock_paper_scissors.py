#------------ Rock Paper Scissors Python ----------------
# Rules:                                                |
# - Rock beats scissors                                 |
# - Scissors beats paper                                |
# - Paper beats rock                                    |
# -------------------------------------------------------

import random

# valid choices
choices = ["rock", "paper", "scissors"]

# welcome message
print("Welcome to Rock-Paper-Scissors!")

# main game loop
while True:
    # get user choice with validation
    user_choice = input("Enter Rock, Paper, or Scissors: ").lower()
    while user_choice not in choices:
        print("Invalid choice! Try again.")
        user_choice = input("Enter Rock, Paper, or Scissors: ").lower()
    
    # get computer choice
    computer_choice = random.choice(choices)

    # show choices
    print(f"You chose: {user_choice}")
    print(f"computer chose: {computer_choice}")

    # check winner
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
         print("You win!")
    else:
         print("Computer wins!")
    
    # ask to play again
    play_again = input("Play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thanks for playing!")
        break
