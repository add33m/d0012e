def max_subarray_sum(array, low, high):
    #Base case if array has one element
    if low == high:
        return array[low]

    #Find the middle index of the array
    mid = (low + high) // 2

    #Recursively find the maximum value in the left and right subarray
    left_max = max_subarray_sum(array, low, mid)
    right_max = max_subarray_sum(array, mid + 1, high)

    #Find the maximum subarray sum that crosses the midpoint
    cross_max = max_crossing_sum(array, low, mid, high)

    #Return the biggest
    return max(left_max, right_max, cross_max)

def max_crossing_sum(arr, low, mid, high):
    #Find the maximum sum of the subarray that crosses the midpoint
    left_sum = 0
    current_sum = 0

    #Loop the left half of the array
    for i in range(mid, low - 1, -1):
        current_sum += arr[i]
        left_sum = max(left_sum, current_sum)

    #Reset for right half
    current_sum = 0
    right_sum = 0

    #Loop the right half of the array
    for i in range(mid + 1, high + 1):
        current_sum += arr[i]
        right_sum = max(right_sum, current_sum)

    #Return the sum of the maximum subarray that crosses the midpoint
    return left_sum + right_sum

#Example
A = [1, -3, 79, 5, -1, 80]


result = max_subarray_sum(A, 0, len(A) - 1)
print(result)