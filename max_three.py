# ----------------------------------
# Max Of Three                     |
# ----------------------------------
# If A is largest → return A       |
# Else if B is largest → return B  |
# Else → return C                  |
# ----------------------------------
def max_of_three(num1, num2, num3):
    maximum = num1
    if num2 > maximum:
        maximum = num2
    if num3 > maximum:
        maximum = num3
    return maximum
# test
print(max_of_three(27, 13, 19))
