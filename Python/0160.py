# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        a, b = headA, headB
        
        while a and b and a != b:
            a, b = a.next, b.next
            if a == b:
                return a
            if not a:
                a = headB
            if not b:
                b = headA

        return a