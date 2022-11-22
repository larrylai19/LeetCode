# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        lessHead, greaterHead = ListNode(), ListNode()
        l, g = lessHead, greaterHead
        
        p = head
        while p:
            if p.val < x:
                l.next = p
                l = l.next
            else:
                g.next = p
                g = g.next
            p = p.next
        
        g.next = None
        l.next = greaterHead.next
        return lessHead.next