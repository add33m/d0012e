
# We may assume that input size n = 3 * 2^(k-1) for some positive int k, i.e. 3, 6, 12, 24 etc.
# With this we can divide in 2 until array is exactly len 3, and return these values in sorted order
# We then perform use a mergesort-like algorithm and always return only the three smallest values

# This algorithm will not run in exactly O(n) but worst-case is approximately linear O(n + log n)

def three_smallest_divcon(list):
    if len(list) == 3:
        # Hardcoded insertionsort for n = 3
        x, y, z = list
        if y < x:
            x, y = y, x
        if z < y:
            y, z = z, y
        if y < x:
            x, y = y, x
    
        return x, y, z
        

    right_of_center = len(list) // 2
    smallest_in_left_half = three_smallest_divcon(list[:right_of_center])
    smallest_in_right_half = three_smallest_divcon(list[right_of_center:])

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
    return tuple(output)

# testlist = [16, 49, 22, 38, 14, 38, 50, 8, 25, 13, 39, 40, 36, 22, 27, 44, 23, 32, 25, 15, 47, 30, 48, 48]
# print(three_smallest_divcon(testlist))
