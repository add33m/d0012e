import timeit as t
import random as r

from bSort import bSortCount

# Run a test given an algorithm and input data, returns "operation count", time taken (secs) and if data is correct
def run_test(algo, data):
  ops_count = algo(data)
  time_delta = t.timeit(lambda: algo(data), number=1)

  i = 0
  result_is_correct = True
  while i < len(data)-1:
    if data[i] > data[i+1]:
      result_is_correct = False
      break
    i += 1

  return ops_count, time_delta, result_is_correct



# Example test run
test = []
i = 0
while i < 2*10**4:
  i += 1
  test.append(r.randint(0, 10**8))
print("Running test")
print(run_test(bSortCount, test))
