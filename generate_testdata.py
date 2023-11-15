import random as r

# To generate:
# - different sizes
# - different levels of sortedness

def insertionSort_special(arr, cmp):
    n = len(arr)  # Get the length of the array
      
    if n <= 1:
        return  # If the array has 0 or 1 element, it is already sorted, so return
 
    for i in range(1, n):  # Iterate over the array starting from the second element
        key = arr[i]  # Store the current element as the key to be inserted in the right position
        j = i-1
        while j >= 0 and (cmp(key, arr[j]) < 0):  # Move elements greater than key one position ahead
            arr[j+1] = arr[j]  # Shift elements to the right
            j -= 1
        arr[j+1] = key  # Insert the key in the correct position

def generate_testdata(size, randomness):
  data = []
  i = 0
  while i < size:
    data.append(r.randint(0, size*2))
    i += 1

  def comparator(a, b):
    flip = 1
    if r.random() < randomness/2:
      flip = -1

    if a < b:
      return -1 * flip
    elif a > b:
      return 1 * flip
    else:
      return 0

  if randomness != 1:
    insertionSort_special(data, comparator)

  return data

# Example data to show different sortedness levels
# print("Unsorted:")
# print(generate_testdata(3*10**1, 1))
# print("Mostly unsorted:")
# print(generate_testdata(3*10**1, .1))
# print("Almost sorted:")
# print(generate_testdata(3*10**1, .02))

def generate_dataset():
  print("Generating dataset...")
  with open("dataset", "w") as f:
    # Generate 24 datasets of completely unsorted random data, sizes 2^3 - 2^24
    print("Generating unsorted data...")
    for size in range(3, 25):
        f.write(str(generate_testdata(2**size, 1)))
        f.write("\n")

    # Generate 24 datasets of mostly unsorted random data, sizes 2^3 - 2^24
    print("Generating mostly unsorted data...")
    for size in range(3, 25):
        f.write(str(generate_testdata(2**size, .1)))
        f.write("\n")

    # Generate 24 datasets of almost sorted random data, sizes 2^3 - 2^24
    print("Generating almost sorted data...")
    for size in range(3, 25):
        f.write(str(generate_testdata(2**size, .02)))
        f.write("\n")

generate_dataset()
