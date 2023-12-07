# Definition for a binary tree node.
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        #Create a helper function to create the tree
        def createTree(nums):
            #If the list is empty
            if not nums:
                #Return None
                return None
            #Find the middle index
            mid = len(nums) // 2
            #Create a node with the value of the middle element
            node = TreeNode(nums[mid])
            #Set the left subtree to the result of calling the helper function on the left half of the list
            node.left = createTree(nums[:mid])
            #Set the right subtree to the result of calling the helper function on the right half of the list
            node.right = createTree(nums[mid+1:])
            #Return the node
            return node
        #Call the helper function
        return createTree(nums)
        