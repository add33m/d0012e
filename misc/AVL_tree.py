import math as m
from radix_sort import radix_sort
from tree_node import TreeNode

# Construct an AVL tree on n distinct integers in the range 0, 1, 2, ... n^3-1. Must run in O(n) in the worst case.
# I will use a simple divide-and-conquer, separating out the middle
# Function returns the root node of the AVL tree
def build_avl_from_sorted(A, n):
    if n < 3:
        root = TreeNode(A[0])
        if n > 1:
            root.setRight(TreeNode(A[1]))

        return root
    
    else:
        middle = m.floor(n/2)
        root = TreeNode(A[middle])
        root.setLeft(build_avl_from_sorted(A[:middle], m.ceil((n-1)/2)))
        root.setRight(build_avl_from_sorted(A[middle+1:], m.floor((n-1)/2)))
        return root
    
def build_avl_special(A, n):
    digits = 3
    base = n
    sorted_A = radix_sort(A, n, digits, base)
    return build_avl_from_sorted(sorted_A, n)

def print_inorder_walk(T):
    if T.l:
        print_inorder_walk(T.l)
    print(T.value)
    if T.r:
        print_inorder_walk(T.r)
        
test = [321, 432, 456, 123, 987, 238, 385, 19, 7, 999]
T = build_avl_special(test, 10)
print_inorder_walk(T)
