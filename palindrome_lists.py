user_string = input("Enter a string: ")
# [::-1] is slicing syntax that reverses a string.
# [::-1] works by:
# - Start: Default (beginning of string)
# - Stop: Default (end of string)
# - Step: -1 (moves backwards)
if user_string ==  user_string[::-1]:
     print("Your word or text is Palindrome")
else:
     print("Your word or text is not Palindrome")
