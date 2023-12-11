# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        slow = head
        fast = head.next
        while slow != fast:
            if fast is None or fast.next is None:
                return False
            slow = slow.next
            fast = fast.next.next
        return True
        

# test 
def create_listnode(nums: list) -> Optional[ListNode]:
    if len(nums) == 0:
        return None
    head = ListNode(nums[0])
    cur = head
    for i in range(1, len(nums)):
        cur.next = ListNode(nums[i])
        cur = cur.next
    return head

def print_listnode(head: Optional[ListNode]):
    cur = head
    while cur is not None:
        print(cur.val, end=' ')
        cur = cur.next
    print()

def test():
    s = Solution()
    head = create_listnode([3,2,0,-4])
    print_listnode(head)
    print(s.hasCycle(head))
    head = create_listnode([1,2])
    print_listnode(head)
    print(s.hasCycle(head))
    head = create_listnode([1])
    print_listnode(head)
    print(s.hasCycle(head))
    head = create_listnode([])
    print_listnode(head)
    print(s.hasCycle(head))

test()
