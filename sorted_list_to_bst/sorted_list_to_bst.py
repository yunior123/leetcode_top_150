from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
            
            if head is None:
                return None
            
            def get_mid(head):
                prev = None
                slow = head
                fast = head
                while fast and fast.next:
                    prev = slow
                    slow = slow.next
                    fast = fast.next.next
                if prev:
                    prev.next = None
                return slow
            
            mid = get_mid(head)
            node = TreeNode(mid.val)
            if head == mid:
                return node
            node.left = self.sortedListToBST(head)
            node.right = self.sortedListToBST(mid.next)
            return node
        