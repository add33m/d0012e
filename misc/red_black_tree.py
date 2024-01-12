import math as m
from radix_sort import radix_sort
from tree_node import RBNode

# Construct an AVL tree on n distinct integers in the range 0, 1, 2, ... n^3-1. Must run in O(n) in the worst case.
# I will use a simple divide-and-conquer, separating out the middle
# Function returns the root node of the AVL tree
def build_rbt_from_sorted(A, n):
    if n < 3:
        root = RBNode(A[0], False)
        if n > 1:
            root.setRight(RBNode(A[1], True))

        return root
    
    else:
        middle = m.floor(n/2)
        root = RBNode(A[middle], False)
        root.setLeft(build_rbt_from_sorted(A[:middle], m.ceil((n-1)/2)))
        root.setRight(build_rbt_from_sorted(A[middle+1:], m.floor((n-1)/2)))
        return root
    
def build_rbt_special(A, n):
    digits = 3
    base = n
    sorted_A = radix_sort(A, n, digits, base)
    return build_rbt_from_sorted(sorted_A, n)

def print_inorder_walk_rbt(T, parent):
    if T.l:
        print_inorder_walk_rbt(T.l, T)
    print(f"Value: {T.value}; Parent: {parent and parent.value}; isRed: {T.isRed}")
    if T.r:
        print_inorder_walk_rbt(T.r, T)
        
test = [321, 432, 456, 123, 987, 238, 385, 19, 7, 999]
T = build_rbt_special(test, 10)
print_inorder_walk_rbt(T, None)