# ------------------ Binary search | Instructions --------------------------
# Function takes an ordered list of numbers (from smallest to largest)     |
# and another number. The function decides whether or not                  |
# the given number is inside the list and returns appropriate boolean.     |
# --------------------------------------------------------------------------

def element_search(num_list, num):
    # Initialize pointers 
    # left set the first index of the list (index 0) 
    # right set to the last index of the list
    left, right = 0, len(num_list) - 1
    # Ensures you check the middle element
    while left <= right:
        # Middle Index: // for integer division to avoid decimals
        mid = (left + right) // 2
        print(f"Checking: left={left}, right={right}, mid={mid}, value={num_list[mid]}")
        if num_list[mid] == num:
            # for an odd list 
            print(True)
            return True
        elif num_list[mid] < num:
            # search right half
            left = mid + 1
        else:
            # search left half 
            right = mid - 1
    print(False)
    return False
# test 
num_list = [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
element_search(num_list, 3)
element_search(num_list, 10)
element_search([], 16)
element_search(num_list, 12)