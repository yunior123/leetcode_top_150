from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # 1. Initialize the dummy node
        dummy = ListNode(0)
        dummy.next = head
        
        # 2. Initialize the prev and curr pointers
        prev = dummy
        curr = dummy.next
        
        # 3. Initialize the counter
        counter = 0
        
        # 4. Reverse the linked list
        while curr:
            counter += 1
            
            if counter % k == 0:
                prev = self.reverse(prev, curr.next)
                curr = prev.next
            else:
                curr = curr.next
        
        return dummy.next
    
    def reverse(self, prev: ListNode, next: ListNode) -> ListNode:
        # 1. Initialize the last node
        last = prev.next
        
        # 2. Initialize the curr pointer
        curr = last.next
        
        # 3. Reverse the linked list
        while curr != next:
            last.next = curr.next
            curr.next = prev.next
            prev.next = curr
            curr = last.next
        
        return last
        