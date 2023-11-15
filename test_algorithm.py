import timeit as t
import random as r

from bSort import bSortCount

# Run a test given an algorithm and input data, returns "operation count", time taken (secs) and if data is correct
def run_test(algo, data):
  ops_count = algo(data)
  time_delta = t.timeit(lambda: algo(data), number=1)

  # Check so sorted array actually is sorted correctly
  result_is_correct = True
  # i = 0
  # while i < len(data)-1:
  #   if data[i] > data[i+1]:
  #     result_is_correct = False
  #     break
  #   i += 1

  return ops_count, time_delta, result_is_correct



# Example test run
# test = []
# i = 0
# while i < 2*10**4:
#   i += 1
#   test.append(r.randint(0, 10**8))
# print(run_test(bSortCount, test))

def run_testset(algo):
  print("Running test...")
  with open("dataset", "r") as f:
    # Generate 24 datasets of completely unsorted random data, sizes 2^3 - 2^24
    print("Testing unsorted data...")
    for size in range(3, 25):
      linedata = f.readline().split(", ")
      # Remove leading "'["
      linedata[0] = linedata[0][2:]

      # Remove trailing "]\n'"
      linedata[-1] = linedata[-1][:-2]

      if size < 10:
        print("Size = ", 2**size, run_test(algo, linedata))

    # Generate 24 datasets of mostly unsorted random data, sizes 2^3 - 2^24
    print("Generating mostly unsorted data...")
    for size in range(3, 25):
      linedata = f.readline().split(", ")
      # Remove leading "'["
      linedata[0] = linedata[0][2:]

      # Remove trailing "]\n'"
      linedata[-1] = linedata[-1][:-2]

      if size < 10:
        print("Size = ", 2**size, run_test(algo, linedata))

    # Generate 24 datasets of almost sorted random data, sizes 2^3 - 2^24
    print("Generating almost sorted data...")
    for size in range(3, 25):
      linedata = f.readline().split(", ")
      # Remove leading "'["
      linedata[0] = linedata[0][2:]

      # Remove trailing "]\n'"
      linedata[-1] = linedata[-1][:-2]

      if size < 10:
        print("Size = ", 2**size, run_test(algo, linedata))

run_testset(bSortCount)
