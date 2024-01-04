from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def dfs(root, path):
            if root is None:
                return
            if root.left is None and root.right is None:
                path.append(str(root.val))
                paths.append("->".join(path))
                path.pop()
                return
            path.append(str(root.val))
            dfs(root.left, path)
            dfs(root.right, path)
            path.pop()
        
        paths = []
        dfs(root, [])
        return paths