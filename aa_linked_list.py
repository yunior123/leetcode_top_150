class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        dummy = ListNode(-1)
        current = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        
        # Attach the remaining nodes from list1 or list2
        current.next = list1 or list2

        return dummy.next

# Helper function to create a linked list from a Python list
def create_linked_list(elements):
    if not elements:
        return None
    head = ListNode(elements[0])
    current = head
    for val in elements[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Helper function to print a linked list
def print_linked_list(head):
    elements = []
    while head:
        elements.append(head.val)
        head = head.next
    print(" -> ".join(map(str, elements)))

# Sample input lists
list1 = create_linked_list([1, 2, 4])
list2 = create_linked_list([1, 3, 4])

# Merge the lists
solution = Solution()
merged_list = solution.mergeTwoLists(list1, list2)

# Print the result
print("Merged List:")
print_linked_list(merged_list)
