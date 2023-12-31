# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        result = True
        if head is None:
            return result
        values = []
        while head:
            values.append(head.val)
            head = head.next
        for i in range(len(values)//2):
            if values[i] != values[len(values)-i-1]:
                result = False
                break
        return result
        