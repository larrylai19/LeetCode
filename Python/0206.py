# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        org_head = head
        curr = head.next
        while curr:
            _next = curr.next
            curr.next = head
            head = curr
            curr = _next
        org_head.next = None
        
        return head