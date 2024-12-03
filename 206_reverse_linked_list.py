from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        result = []
        current = self
        while current:
            result.append(str(current.val))
            current = current.next
        return " -> ".join(result)

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_list = None
        current = head

        while current:
            next_node = current.next  # Save the next node
            current.next = new_list  # Reverse the link
            new_list = current       # Move new_list pointer to current node
            current = next_node      # Move current to the next node
    
        return new_list

def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

solution = Solution()

head1 = create_linked_list([1, 2, 3, 4, 5])
print("Original:", head1)
reversed1 = solution.reverseList(head1)
print("Reversed:", reversed1)
