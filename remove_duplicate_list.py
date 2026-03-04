# -----------------------------------------------------------------
# Write a function that takes a list and returns a new list that. |
# contains all the elements of the first list minus duplicates.   |
#------------------------------------------------------------------

# The first function using for loop and set to speed up the check
def remove_duplicate(input_list):
    # seen track elements we’ve already encountered in the input list
    # making the duplicate check much faster
    seen = set()
    unique_list = []
    for item in input_list:
        # see speed up the duplicate check
        if item not in seen:
            seen.add(item)
            unique_list.append(item)
    return unique_list

# The function is short and only using set 
# but doesn't preserve the orignal order. 
def dedupe_list(lst):
    return list(set(lst))

# test
A_list = [12, 5, 5, 9, 8, 17, 20, 1, 3, 3, 11, 10, 11]
print(remove_duplicate(A_list))
print(dedupe_list(A_list))  