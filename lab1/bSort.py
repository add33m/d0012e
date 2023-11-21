
# Perform a binary search, returning the index where the new value should be inserted
def binSearch(list, loBound, upBound, item):
  while upBound - loBound >= 1:
    i = (loBound + upBound) // 2
    comparator = list[i]

    if item == comparator:
      return i
    elif item < comparator:
      # Item is less than comparator
      upBound = i - 1
    else:
      # Item is larger than comparator
      loBound = i + 1

  if item < list[loBound]:
    return loBound
  else:
    return loBound+1
  
# Binary search with code iteration counter
def binSearchCount(list, loBound, upBound, item):
  counter = 1
  while upBound - loBound >= 1:
    counter += 1

    i = (loBound + upBound) // 2
    comparator = list[i]

    if item == comparator:
      return i, counter
    elif item < comparator:
      # Item is less than comparator
      upBound = i - 1
    else:
      # Item is larger than comparator
      loBound = i + 1

  if item < list[loBound]:
    return loBound, counter
  else:
    return loBound+1, counter

# Perform an insertionsort using binary search (binary insertion sort/bSort)
def bSort(list):
  n = len(list)
  i = 1
  
  while i < n:
    # Get the item to sort
    itemToSort = list[i]

    # Find position to insert into
    newPos = binSearch(list, 0, i-1, itemToSort)

    # Move over items above new pos, and insert item to its sorted position
    list[newPos:i+1] = [itemToSort] + list[newPos:i]

    i += 1

# Bsort with code iteration counter
def bSortCount(list):
  counter = 1
  n = len(list)
  i = 1

  while i < n:
    # Get the item to sort
    itemToSort = list[i]

    # Find position to insert into
    newPos, iterations = binSearchCount(list, 0, i-1, itemToSort)

    # Move over items above new pos, and insert item to its sorted position
    list[newPos:i+1] = [itemToSort] + list[newPos:i]

    counter += iterations + 1
    i += 1

  return counter


# arr = [12, 11, 13, 5, 6]
# print("Iterations:", bSortCount(arr))
# print(arr)
