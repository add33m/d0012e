import insertionSort
import bSort


def merge_sort(list):

  if len(list) <= 5:
    print("whoop")
    insertionSort(list)
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