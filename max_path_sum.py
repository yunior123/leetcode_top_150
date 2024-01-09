from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            nonlocal max_sum
            if not node:
                return 0
            
            left = max(dfs(node.left), 0)
            right = max(dfs(node.right), 0)
            
            max_sum = max(max_sum, node.val + left + right)
            
            return node.val + max(left, right)
        
        max_sum = float('-inf')
        dfs(root)
        
        return max_sum
        