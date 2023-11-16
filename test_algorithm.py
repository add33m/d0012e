import timeit as t
import random as r

from bSort import bSortCount
from mergeSort2 import mergesort2CountI, mergesort2CountB

# Run a test given an algorithm and input data, returns "operation count", time taken (secs) and if data is correct
def run_test(algo, data, k):
  ops_count = [0]

  def test():
    ops_count[0] = algo(data, k)[1]

  time_delta = t.timeit(test, number=1)

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
        csv.write("size, k2, k8, k32, k128, k256\n")

        # Read all the sizes
        for size in range(3, 25):
          if size < 19:
            linedata = f.readline().split(", ")
            # Remove leading "'["
            linedata[0] = linedata[0][2:]

            # Remove trailing "]\n'"
            linedata[-1] = linedata[-1][:-2]
            line = str(2**size) + ","
            line += str(run_test(algo, linedata, 2)[0]) + ","
            line += str(run_test(algo, linedata, 8)[0]) + ","
            line += str(run_test(algo, linedata, 32)[0]) + ","
            line += str(run_test(algo, linedata, 128)[0]) + ","
            line += str(run_test(algo, linedata, 256)[0]) + "\n"
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
print("I")
run_testset(mergesort2CountI, "ins")
print("B")
run_testset(mergesort2CountB, "bin")
