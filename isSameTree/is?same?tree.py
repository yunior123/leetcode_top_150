# Definition for a binary tree node.
from typing import List, Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #Create a helper function to traverse the trees
        def traverse(p, q):
            #If both nodes are null
            if not p and not q:
                #Return True
                return True
            #If one node is null
            if not p or not q:
                #Return False
                return False
            #If the values of the nodes are not equal
            if p.val != q.val:
                #Return False
                return False
            #Return the result of traversing the left subtree and the right subtree
            return traverse(p.left, q.left) and traverse(p.right, q.right)
        #Call the helper function
        return traverse(p, q)
        