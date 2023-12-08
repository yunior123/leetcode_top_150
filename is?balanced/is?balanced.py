from typing import List, Optional
# Height-Balanced
# A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        #Create a helper function to find the height of the tree
        def height(node):
            #If the node is null
            if not node:
                #Return 0
                return 0
            #Return 1 plus the maximum of the height of the left subtree and the height of the right subtree
            return 1 + max(height(node.left), height(node.right))
        #If the root is null
        if not root:
            #Return True
            return True
        #If the absolute value of the difference between the height of the left subtree and the height of the right subtree is greater than 1
        if abs(height(root.left) - height(root.right)) > 1:
            #Return False
            return False
        #Return the result of calling the function on the left subtree and the right subtree
        return self.isBalanced(root.left) and self.isBalanced(root.right)
      