import math as m

def radix_sort(A, n, d, base):
    array = A
    # For each digit (starting with the LSD going to MSD)
    for i in range(d):
        # Create a function that gives only the relevant digit
        f = lambda x: m.floor(x / base**i) % base
        array = counting_sort(array, n, base, f)
        
    return array
        

# Sorts A in O(n+k)
# This is modified to take a function that determines the actual number we want to use to sort
# so that we can sort on one digit at a time (for radix sort above)
def counting_sort(A, n, k, f):
    # Create an array of all 0s, as long as the amount of different numbers we can have (k)
    # In this array, we will count how many input values are equal to all of the different numbers
    amount_equal_to = [0]*k
    
    # Count how many input values are equal to the different possible numbers (0 ... k)
    for number in A:
        amount_equal_to[f(number)] += 1
    
    # Array similar to the first, but now counting equal to or less than    
    amount_eqlt = [0]*k
    # No numbers are allowed to be less than 0, so equal to or less than 0 is just amount equal to 0.
    amount_eqlt[0] = amount_equal_to[0]
    for i in range(1, k):
        # Amount equal to or less than a certain number is the amount eqlt the previous number + the amount equal to the number
        amount_eqlt[i] = amount_equal_to[i] + amount_eqlt[i-1]
        
    # Create a new array to copy over into, as large as the input (A)
    result = [None]*n

    # Put each number at the appropriate position
    # (if 10 numbers are equal to or less than Ai, put Ai at position 10 (index 10-1=9) in result since one of those is the number itself)
    # We go backwards and then decrement by one in amount_eqlt to handle duplicates
    for value in A[::-1]:
        result[amount_eqlt[f(value)]-1] = value
        amount_eqlt[f(value)] -= 1
        
    return result
    
# test = [321, 432, 456, 123, 987]
# print(radix_sort(test, len(test), 3, 10))
