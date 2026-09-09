user_input = int(input("Enter number of seconds: "))
remain = user_input // 60 
seconds = user_input % 60
print(f"{user_input} seconds = {remain} minutes and {seconds} seconds")
