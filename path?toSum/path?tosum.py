from typing import List, Optional
# Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        #Create a helper function to traverse the tree
        def traverse(node, targetSum):
            #If the node is null
            if not node:
                #Return False
                return False
            #If the node is a leaf node and the value of the node is equal to the target sum
            if not node.left and not node.right and node.val == targetSum:
                #Return True
                return True
            #Return the result of traversing the left subtree and the right subtree
            return traverse(node.left, targetSum - node.val) or traverse(node.right, targetSum - node.val)
        #Call the helper function
        return traverse(root, targetSum)

        