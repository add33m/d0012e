
# Binary search, return
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

    if item < list[i]:
      return loBound
    else:
      return upBound


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


arr = [12, 11, 13, 5, 6]
bSort(arr)
print(arr)

# class Hello:
#   def __init__(self, arg1, arg2):
#     pass

#   def sayHi(self):
#     print("Hi!")

# Hello().sayHi()