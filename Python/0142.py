# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dup = set()
        node = head
        while node:
            if node in dup:
                return node
            dup.add(node)
            node = node.next
        return None