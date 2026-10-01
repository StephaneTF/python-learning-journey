# ------------------- Reverse Word Order Instructions --------------------------
# Write a program (using functions!) that asks the user for a long string      |
# containing multiple words. Print back to the user the same string,           |
# except with the words in backwards order.                                    |
# ------------------------------------------------------------------------------
# Python list representation: [start : end]                                    |
# slicing method: [start : end : step]                                         |
# where step controls the direction and increment.                             |
# ------------------------------------------------------------------------------

# Reverse word function.
def reverse_words():
    while True:
        long_string = input("Enter a long string with multiple words: ")
        words = long_string.split()

        # Input validation: require at least two words
        if len(words) < 2:
            print("Please enter at least two words.")
            continue

        reversed_words = words[::-1]
        reversed_string = " ".join(reversed_words)
        return reversed_string


# Play again logic
print("******* Words Order Reverser *******")

while True:
    result = reverse_words()
    print("Reversed word order:", result)

    play_again = input("Play again? (yes/no): ").lower()

    if play_again != "yes":
        print("Thanks for playing!")
        break