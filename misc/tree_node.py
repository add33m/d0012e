class TreeNode:
    value, l, r = None, None, None 
    def __init__(self, val):
        self.value = val
        
    def setLeft(self, node):
        self.l = node

    def setRight(self, node):
        self.r = node
        
class RBNode(TreeNode):
    isRed = False
    def __init__(self, val, red):
        self.isRed = red
        super().__init__(val)