import random as r

# To generate:
# - different sizes
# - different levels of sortedness

def generate_testdata(size, sortedness):
  data = []
  i = 0
  while i < size:
    data.append(r.randint(0, size*2))
    i += 1

  def comparator(a, b):
    flip = 1
    if r.random < sortedness/2:
      flip = -1

    if a < b:
      return -1 * flip
    elif a > b:
      return 1 * flip
    else:
      return 0

  data = sorted(data, cmp)

  return data

print(generate_testdata(10**1, .1))
