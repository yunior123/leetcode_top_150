# Definition for a binary tree node.
from typing import List, Optional

# Input: root = [1,null,2,3]
# Output: [1,3,2]
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #Create a list to store the values
        values = []
        #Create a helper function to traverse the tree
        def traverse(node):
            #If the node is not null
            if node:
                #Traverse the left subtree
                traverse(node.left)
                #Add the value of the node to the list
                values.append(node.val)
                #Traverse the right subtree
                traverse(node.right)
        #Call the helper function
        traverse(root)
        #Return the list
        return values