# --------------------------------- Fibonacci Python ----------------------------
# The Fibonacci sequence is a series of numbers                                 |
# where each number is the sum of the two numbers before it.                    |
# -------------------------------------------------------------------------------
# How It Works                                                                  |
# Start with 1 and 1.                                                           |
# Add them to get the next number: 1 + 1 = 2.                                   |
# Keep adding the last two numbers to get the next one.                         |
# Rule: F(n) = F(n-1) + F(n-2)                                                  |
# -------------------------------------------------------------------------------

# Get and validate the number from the user.
def get_number():
    while True:
        number = int(input("How many Fibonacci numbers? "))
        if number <= 0:
            print("Please enter a positive number.")
            continue
        if number > 100:
            print("Please enter a number less than or equal to 100.")
            continue
        return number

# Define Fibonacci function.
def fibonacci(n):
    if n == 1:
        return [1]
    # Start the sequence with 1 and 1.
    fib = [1, 1]
    # Generate the remaining Fibonacci numbers.
    for i in range(2, n):
        fib.append(fib[i - 1] + fib[i - 2])
    return fib

# Main program loop allows replay.
while True:
    number = get_number()
    print(f"Fibonacci sequence: {fibonacci(number)}")
    play_again = input("Play again? (Yes/No): ")
    # Makes the input case-insensitive.
    if play_again.lower() != "yes":
        print("Thanks for playing!")
        break