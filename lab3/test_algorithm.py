import timeit as t
import math as m

from D import Node

# Run a test given an algorithm and input data, returns "operation count", time taken (secs) and if data is correct
def run_test(data, c, amount=1):
  
  def test():
    master = Node(data.pop())
    for value in data:
      master.insert_node(value, c)

  time_delta = t.timeit(test, number=amount)

  return time_delta


def run_testset(name):
  print("Running test...", name)
  with open("lab3/dataset", "r") as f:
    
    print("Unsorted:")
    # Open a file to write results to
    with open(f"lab3/{name}_us.csv", "w") as csv:
      # Write header for csv
      csv.write("size,c.5,c.6,c.7,c.8,c.9,c1\n")

      # Unsorted data
      for size in range(3, 25):
        if 5 < size < 16:
          linedata = f.readline().split(", ")

          # Remove leading "'["
          linedata[0] = linedata[0][2:]
          # Remove trailing "]\n'"
          linedata[-1] = linedata[-1][:-2]

          line = str(2**size) + ","
          line += str(run_test(linedata, .5)) + ","
          line += str(run_test(linedata, .6)) + ","
          line += str(run_test(linedata, .7)) + ","
          line += str(run_test(linedata, .8)) + ","
          line += str(run_test(linedata, .9)) + ","
          line += str(run_test(linedata, 1)) + "\n"
          print("Tested", name, 2**size)
          print(line[:-1])
          csv.write(line)

        else:
          f.readline()

    print("Sorted:")
    # Open a file to write results to
    with open(f"lab3/{name}_s.csv", "w") as csv:
      # Write header for csv
      csv.write("size,c.5,c.6,c.7,c.8,c.9,c1\n")

      # Unsorted data
      for size in range(3, 25):
        if 5 < size < 16:
          linedata = f.readline().split(", ")

          # Remove leading "'["
          linedata[0] = linedata[0][2:]
          # Remove trailing "]\n'"
          linedata[-1] = linedata[-1][:-2]

          line = str(2**size) + ","
          line += str(run_test(linedata, .5)) + ","
          line += str(run_test(linedata, .6)) + ","
          line += str(run_test(linedata, .7)) + ","
          line += str(run_test(linedata, .8)) + ","
          line += str(run_test(linedata, .9)) + ","
          line += str(run_test(linedata, 1)) + "\n"
          print("Tested", name, 2**size)
          print(line[:-1])
          csv.write(line)

        else:
          f.readline()

# Generate 24 datasets of completely unsorted random data, sizes 2^3 - 2^24
# run_testset("b_tree_insert_times")

# run_testset(bSortCount)
# print("I")
# run_testset(mergesort2CountI, "ins")
# print("B")
# run_testset(mergesort2CountB, "bin")

# Find optimal k
def show_diminish():
  print("Generating c graph...")
  with open("lab3/dataset", "r") as f:

    # Unsorted data
    for size in range(3, 25):
      if size == 12:
        linedata = f.readline().split(", ")
        # Remove leading "'["
        linedata[0] = linedata[0][2:]

        # Remove trailing "]\n'"
        linedata[-1] = linedata[-1][:-2]
        
        # Create csv with values
        with open(f"lab3/b_tree_c_times_us.csv", "w") as csv:
          csv.write("c,time\n")
          c = .5
          while c <= 1:
            time_taken = run_test(linedata, c, 10)/10
            csv.write(f"{c},{time_taken}\n")
            print("Tested c = ", c, "; Time = ", time_taken)
            c = round(c+.02, 2)

      else:
        f.readline()

    # Sorted data
    for size in range(3, 25):
      if size == 12:
        linedata = f.readline().split(", ")
        # Remove leading "'["
        linedata[0] = linedata[0][2:]

        # Remove trailing "]\n'"
        linedata[-1] = linedata[-1][:-2]
        
        # Create csv with values
        with open(f"lab3/b_tree_c_times_s.csv", "w") as csv:
          csv.write("c,time\n")
          c = .5
          while c <= 1:
            time_taken = run_test(linedata, c, 10)
            csv.write(f"{c},{time_taken}\n")
            print("Tested c = ", c, "; Time = ", time_taken)
            c = round(c+.02, 2)

      else:
        f.readline()

show_diminish()
