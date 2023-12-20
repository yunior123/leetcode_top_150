from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
            
            if not head:
                return None
            
            while head and head.val == val:
                head = head.next
            
            if not head:
                return None
            
            head.next = self.removeElements(head.next, val)
            
            return head
        