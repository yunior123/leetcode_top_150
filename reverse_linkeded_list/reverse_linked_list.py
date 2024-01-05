from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        if head is None:
            return None
        
        dummy = ListNode(next=head)
        prev = dummy
        curr = head
        for _ in range(left-1):
            prev = curr
            curr = curr.next
        
        for _ in range(right-left):
            next = curr.next
            curr.next = next.next
            next.next = prev.next
            prev.next = next
        
        return dummy.next