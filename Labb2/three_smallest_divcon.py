
# We may assume that input size n = 3 * 2^(k-1) for some positive int k, i.e. 3, 6, 12, 24 etc.
# With this we can divide in 2 until array is exactly len 3, and return these values in sorted order
# We then perform use a mergesort-like algorithm and always return only the three smallest values

# This algorithm will not run in exactly O(n) but worst-case is approximately linear O(3n + 3 * log n) ~ O(n)
# Exact number of comparisons will be the following:
#   n [for bottom-level insertionsort] + 3 * (k-1) [for mergesort]

# n = 3 * 2^(k-1)
# log2(n / 3) + 1 = k

# k = 4
# 3 * 2^3 = 3*8 = 24
# 24 + 3*7 = 24 + 21

# Proof (induction):
# 1. Base case: k = 1 <=> n = 3
# Returns a sorted version of the list, i.e. x < y < z
# 2. Assume that the algorithm is correct for all k = 1, ..., p
# 3. Show that the algo is correct for k = p + 1  =>  k > 1 <=> n > 3
# In this case, the list will be divided in two halves, each with length n / 2
# n = 3 * 2^(k-1) = 3 * 2^(p+1 - 1) = 3 * 2^p = 2 * (3 * 2^(p-1))
# Any list of n = 3 * 2^(k-1), where 1 <= k <= p will produce a sorted list of three elements,
# Therefore a list of n = 2 * (3 * 2^(p-1)) can be divided into two lists of n = 3 * 2^(p-1)
# From which two sorted lists of n = 3 each can be produced
# We then run mergesort on these two, discarding the top 3 values and keeping the bottom 3
# This will produce a sorted list of 3 elements
# Therefore, the algo will produce a sorted list of 3 elements for all (natural) values of k >= 1

# n = 3 => 4 = 4
# n = 6 => 1 + 4 + 4 + 3 = 12
# n = 12 => 1 + 1 + 1 + 4 + 4 + 4 + 4 + 3 + 3 + 3 = 28
# n = 24 => 1 + 1 + 1 + 1 + 1 + 1 + 1 + 4 + 4 + 4 + 4 + 4 + 4 + 4 + 4 + 3 + 3 + 3 + 3 + 3 + 3 + 3 = 60
# n = 3 * 2^(k-1) => (2^k-1)*1 + 2^k*4 + (2^k-1)*3 = 2^k*4 + (2^k-1)*4 = 4*(2*2^k-1) = 2^(k+2) - 4
# C(k) = 2^(k+2) - 4
# k = log2(n / 3) + 1
# C(n) = 2^(log2(n / 3) + 1 + 2) - 4
# C(n) = 2^(log2(n / 3) + 3) - 4
# C(n) = 2^(log2(n/3))*2^3 - 4
# C(n) = (8/3)*n - 4

       #
   #       #
 #   #   #   #
# # # # # # # #

def three_smallest_divcon(list):
    counter = 4
    if len(list) == 3:
        # Hardcoded insertionsort for n = 3
        x, y, z = list
        if y < x:
            x, y = y, x
        if z < y:
            y, z = z, y
        if y < x:
            x, y = y, x
    
        return (x, y, z), counter
        

    right_of_center = len(list) // 2
    smallest_in_left_half, l_counter = three_smallest_divcon(list[:right_of_center])
    smallest_in_right_half, r_counter = three_smallest_divcon(list[right_of_center:])

    # Perform a simple mergesort of the 6 values we have
    left_counter = 0
    right_counter = 0
    output = []
    while len(output) < 3:
        if smallest_in_left_half[left_counter] < smallest_in_right_half[right_counter]:
            output.append(smallest_in_left_half[left_counter])
            left_counter += 1
        else:
            output.append(smallest_in_right_half[right_counter])
            right_counter += 1
    
    # Return output converted to tuple
    return tuple(output), counter + l_counter + r_counter

# testlist = [16, 49, 22, 38, 14, 38, 50, 8, 25, 13, 39, 40, 36, 22, 27, 44, 23, 32, 25, 15, 47, 30, 48, 48]
# print(three_smallest_divcon(testlist))
