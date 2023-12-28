from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
            
            num_nodes = 0
            
            def count_nodes(node):

                if node is not None:
                    nonlocal num_nodes
                    num_nodes += 1

                    count_nodes(node.left)
                    count_nodes(node.right)
            
        
            count_nodes(root)

            return num_nodes
        