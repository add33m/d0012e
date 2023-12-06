# This algorithm runs in O(n-1)
def max_cross_divcon(list):
  # Vals to calculate
  # msas (Maximum SubArray Sum), msas_l (msas that touches left edge), msas_r (msas that touches right edge), tot

  if len(list) == 2:
    # This is just a simpler case of the same calculations as below
    msas = max(list[0], list[1], list[0] + list[1])
    msas_l = max(list[0], list[0] + list[1])
    msas_r = max(list[1], list[0] + list[1])
    tot = list[0] + list[1]

    return msas, msas_l, msas_r, tot

  # Generate all lower vals for left and right halfs recursively
  mid = len(list) // 2
  left_msas, left_msas_l, left_msas_r, left_tot = max_cross_divcon(list[:mid])
  right_msas, right_msas_l, right_msas_r, right_tot = max_cross_divcon(list[mid:])

  # total MSAS is either left MSAS or right MSAS or total of both lower MSASes touching the middle
  # This is because the msas will either be only in the left half or only the right half or cross the middle, there are no other possibilities 
  msas = max(left_msas, right_msas, left_msas_r + right_msas_l)
  # MSAS touching the left edge is either only left half's left edge MSAS or ALL of the left half + right half's left edge MSAS
  msas_l = max(left_msas_l, left_tot + right_msas_l)
  # Same respectively for right edge msas
  msas_r = max(right_msas_r, right_tot + left_msas_r)
  # Total is just sum of both halves' totals
  tot = left_tot + right_tot

  return msas, msas_l, msas_r, tot

# max(a, b) runs 1 comparison
# max(a, b, c) runs 2 comparisons
# Total comparisons for k:
# k=1 => 5 = 5
# k=2 => 1 + 5 + 5 + 4 = 15
# k=3 => 1 + 1 + 1 + 5 + 5 + 5 + 5 + 4 + 4 + 4 = 35
# comp(k) = (2^k - 1) * 5
# n = 2^k
# k = log2(n)
# comp(k) = (2^log2(n) - 1) * 5 = n-1 * 5

test = [-1, -1, -1, 10, -5, 10, -1, -1]
test1 = [16, -17, 6, -2, 19, -18, 4, 1, 15, -1, -1, -1, -1, -1, -1, 1]
test2 = [1, -3, 79, 5, -1, 80, 2, 9]

print("MSAS:", max_cross_divcon(test)[0])
