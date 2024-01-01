
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        result = None
        if lists:
            values = []
            for i in range(len(lists)):
                while lists[i]:
                    values.append(lists[i].val)
                    lists[i] = lists[i].next
            values.sort(reverse=True)
            for i in range(len(values)):
                result = ListNode(values[i], result)
        return result
        