import random as r

def generate_testdata(size, sorted):
  data = []
  i = 0
  while i < size:
    data.append(r.randint(0, size*2))
    i += 1
  
  if sorted:
    data.sort()

  return data

def generate_dataset():
  print("Generating dataset...")
  with open("dataset", "w") as f:
    # Generate 24 datasets of completely unsorted random data, sizes 2^3 - 2^24
    print("Generating unsorted data...")
    for size in range(3, 25):
        f.write(str(generate_testdata(2**size, False)))
        f.write("\n")
        
    print("Generating sorted data...")
    for size in range(3, 25):
        f.write(str(generate_testdata(2**size, True)))
        f.write("\n")
    

generate_dataset()
