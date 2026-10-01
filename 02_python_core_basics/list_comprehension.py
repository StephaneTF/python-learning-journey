import random

random_number = random.sample(range(0, 50), 27)
print("Enter numbers from this list, separated by spaces:\n", random_number)

# take user input as a list of number 
user_input = input("Enter numbers: ")

# convert input string into list of integer
# with list, map and split functions
user_number = list(map(int, user_input.split()))

# list that has only even number
new_number = [num for num in user_number if num % 2 == 0]
print("Even number from your input: ", new_number)
