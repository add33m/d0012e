# General node object with left/right stores
class Node:
  # Left/right values can be other nodes or None (null)
  l, l_size = None, 0
  r, r_size = None, 0
  val = None

  def __init__(self, value, left_node=None, right_node=None):
    # Set self's value
    self.val = value

    # Set right/left nodes
    if left_node:
      self.l = left_node
    if right_node:
      self.r = right_node

  # Getters to make code more intuitive
  def get_value(self):
    return self.val
  
  def traverse_left(self):
    return self.l
  
  def traverse_right(self):
    return self.r
  
  # Add subtree to given array as a sorted list recursively
  def collect_sorted_leaves(self, collection):
    # First, add all values left of (less than) our value
    if self.l:
      self.l.collect_sorted_leaves(collection)
    
    # Add our value in the middle
    collection.append(self.val)

    # Finally, add all values right of (larger than) our value
    if self.r:
      self.r.collect_sorted_leaves(collection)

  # Recursive functions to calculate size of subtrees/total tree
  def get_size_left(self):
    return self.l_size
  
  def get_size_right(self):
    return self.r_size
  
  def get_size(self):
    return self.l_size + self.r_size + 1
    
  def rebalance(self):
    # Gather all leaves to be rebalanced in a sorted array
    leaves = []
    self.collect_sorted_leaves(leaves)

    replacement = create_subtree(leaves)
    # Reassign self to the replacement
    self.val = replacement.val
    self.l = replacement.l
    self.r = replacement.r


  # Recursive functions to add a new node to the left/right tree
  def insert_node(self, value, c):
    pass
    # TODO:
    # - Increase left/right counter to prevent having to recalculate size
    # - Insert new node at appropriate place (move nodes around if necessary)
    # - Rebalance if necessary (if subtrees are too unbalanced, c determines the limit for this)

# Recursive helper function to perform rebalancing of tree by creating a subtree from a given list of included children/leaves
def create_subtree(children):
  center = len(children) // 2
  node = Node(children[center])
  
  if len(children) > 1:
    # Create left/right halves of the tree recursively
    left_half = children[:center]
    if len(left_half) > 0:
      left_node = create_subtree(left_half)
      node.l = left_node
      node.l_size = len(left_half)

    right_half = children[center+1:]
    if len(right_half) > 0:
      right_node = create_subtree(right_half)
      node.r = right_node
      node.r_size = len(right_half)

  return node

  
# n = Node(1, 2)
# n2 = Node(n)
# print("n2.l.r", n2.l.r)
# print("n2.get_size()", n2.get_size())

# test_tree = create_subtree([0, 0, 2, 5, 6, 9, 10])
# print(test_tree.get_size())
# print(test_tree.l.r.val)
