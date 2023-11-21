import timeit as t
import random as r
import math as m

from bSort import bSortCount
from mergeSort2 import mergesort2CountI, mergesort2CountB

# Run a test given an algorithm and input data, returns "operation count", time taken (secs) and if data is correct
def run_test(algo, data, k, amount=1):
  ops_count = [0]

  def test():
    ops_count[0] = algo(data, k)[1]

  time_delta = t.timeit(test, number=amount)

  return ops_count[0], time_delta



# Example test run
# test = []
# i = 0
# while i < 2*10**4:
#   i += 1
#   test.append(r.randint(0, 10**8))
# print(run_test(bSortCount, test))

def run_testset(algo, name):
  print("Running test...", name)
  with open("dataset", "r") as f:
    # Local func to run same code thrice
    def _test(type):
      # Open a file to write results to
      with open(f"{name}_{type}.csv", "w") as csv:
        # Write header for csv
        csv.write("size,k1,k10,k.1n,k.5n,kn\n")

        # Read all the sizes
        for size in range(3, 25):
          if 5 < size < 16:
            linedata = f.readline().split(", ")
            # Remove leading "'["
            linedata[0] = linedata[0][2:]

            # Remove trailing "]\n'"
            linedata[-1] = linedata[-1][:-2]
            line = str(2**size) + ","
            line += str(run_test(algo, linedata, 1)[1]) + ","
            line += str(run_test(algo, linedata, 10)[1]) + ","
            line += str(run_test(algo, linedata, m.floor(.1*2**size))[1]) + ","
            line += str(run_test(algo, linedata, m.floor(.5*2**size))[1]) + ","
            line += str(run_test(algo, linedata, 2**size)[1]) + "\n"
            print("Tested", name, type, 2**size)
            print(line)
            csv.write(line)

            # print("Size = ", 2**size, "\tk = 2", run_test(algo, linedata, 2))
            # print("Size = ", 2**size, "\tk = 8", run_test(algo, linedata, 8))
            # print("Size = ", 2**size, "\tk = 32", run_test(algo, linedata, 32))
            # print("Size = ", 2**size, "\tk = 128", run_test(algo, linedata, 128))
            # print("Size = ", 2**size, "\tk = 256", run_test(algo, linedata, 256))

            # Find optimal k for this dataset, size 12
            # if size == 12:
            #   k = 0
              
            #   while k < 2**size:
            #     k += 1
            #     run_test()

          else:
            f.readline()

    # Generate 24 datasets of completely unsorted random data, sizes 2^3 - 2^24
    print("Testing unsorted data...")
    _test("us")

    # Generate 24 datasets of mostly unsorted random data, sizes 2^3 - 2^24
    print("Testing mostly unsorted data...")
    _test("mus")

    # Generate 24 datasets of almost sorted random data, sizes 2^3 - 2^24
    print("Testing almost sorted data...")
    _test("as")

# run_testset(bSortCount)
# print("I")
# run_testset(mergesort2CountI, "ins")
# print("B")
# run_testset(mergesort2CountB, "bin")

# Find optimal k
def optimize_k(algo, name):
  print("Optimizing k...", name)
  with open("dataset", "r") as f:
    # Local func to run same code thrice
    def _test(type):
      # Read all the sizes
      for size in range(3, 25):
        if 9 < size < 11:
          linedata = f.readline().split(", ")
          # Remove leading "'["
          linedata[0] = linedata[0][2:]

          # Remove trailing "]\n'"
          linedata[-1] = linedata[-1][:-2]
          
          # Divide-and-conquer to find optimal k by looking in the half where delta between border and middle point is lowest
          # upper_bound = 2**(size-1)
          # lower_bound = 1
          # upper = run_test(algo, linedata, upper_bound, 5)[1]
          # lower = run_test(algo, linedata, lower_bound, 5)[1]
          # middle = run_test(algo, linedata, (upper_bound+lower_bound)//2, 5)[1]

          # while upper_bound - lower_bound > 1:
          #   if abs(upper-middle) < abs(lower - middle):
          #     # Choose upper half
          #     lower = middle
          #     lower_bound = (upper_bound+lower_bound) // 2
          #   else:
          #     # Choose lower half
          #     upper = middle
          #     upper_bound = (upper_bound+lower_bound) // 2

          #   middle = run_test(algo, linedata, (upper_bound+lower_bound)//2, 5)[1]

          # For loop based k optimizer
          # k = 1
          # bestK = 1
          # bestTime = 9999999999
          # while True:
          #   currentTime = run_test(algo, linedata, k, 100)[1]
          #   if currentTime < bestTime:
          #     bestTime = currentTime
          #     bestK = k
          #   elif currentTime > bestTime * 1.06:
          #     break

          #   k += 1
            
          # print(f"Optimal k for size {2**size} =", bestK, "with time", bestTime, ", tested up to k =", k)

          # Create csv with values
          with open(f"{name}_k_optimize.csv", "w") as csv:
            csv.write("k,time\n")
            k = 1
            while k <= 2**size:
              time_taken = run_test(algo, linedata, k, 10)[1]
              csv.write(f"{k},{time_taken}\n")
              k += 1

        else:
          f.readline()

    # Generate 24 datasets of completely unsorted random data, sizes 2^3 - 2^24
    print("Testing unsorted data...")
    _test("us")

    # Generate 24 datasets of mostly unsorted random data, sizes 2^3 - 2^24
    # print("Testing mostly unsorted data...")
    # _test("mus")

    # Generate 24 datasets of almost sorted random data, sizes 2^3 - 2^24
    # print("Testing almost sorted data...")
    # _test("as")

print("I")
optimize_k(mergesort2CountI, "ins")
print("B")
optimize_k(mergesort2CountB, "bin")
