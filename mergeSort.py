

def insertionSort2(arr):
    n = len(arr)  # Get the length of the array
      
    if n <= 1:
        return  # If the array has 0 or 1 element, it is already sorted, so return
 
    for i in range(1, n):  # Iterate over the array starting from the second element
        key = arr[i]  # Store the current element as the key to be inserted in the right position
        j = i-1
        while j >= 0 and key < arr[j]:  # Move elements greater than key one position ahead
            arr[j+1] = arr[j]  # Shift elements to the right
            j -= 1
        arr[j+1] = key  # Insert the key in the correct position

def merge_sort(list):

  if len(list) <= 5:
    print("whoop")
    insertionSort2(list)
    return list

  mid = len(list) // 2

  left_values = merge_sort(list[:mid])

  right_values = merge_sort(list[mid:])

  l = []

  i = 0

  j = 0

  while i < len(left_values) and j < len(right_values):

    if left_values[i] < right_values[j]:

      l.append(left_values[i])

      i += 1

    else:
      l.append(right_values[j])
      j += 1

  l += left_values[i:]
  l += right_values[j:]

  return l


newList = [5,3,1,2,6,4,9,7,8]

print(newList)

print(merge_sort(newList))