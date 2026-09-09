user_number = int(input("Enter a number: "))
num = int(input("Enter another number: "))
check = int(input("Checker:"))
if user_number % 2 == 0:
    print("Your number ", user_number, " is even.")
else:
    print("Your number ", user_number, " is odd.")

if user_number % 4 == 0:
    print(user_number, " is a multiple of 4.")

if num % check == 0:
    print(check, " divides evenly into ", num, ".")
else:
    print(check, " not divides evenly into ", num, ".")