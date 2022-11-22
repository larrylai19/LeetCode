# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        h, m = self.divide(head)
        return self.merge(self.sortList(h), self.sortList(m))
        
    def divide(self, head):
        pre = slow = fast = head
        
        while fast and fast.next:
            pre = slow
            slow = slow.next
            fast = fast.next.next
        
        pre.next = None
        return head, slow
    
    def merge(self, n1, n2):
        if not n1:
            return n2
        if not n2:
            return n1
        
        if n1.val < n2.val:
            n1.next = self.merge(n1.next, n2)
            return n1
        
        n2.next = self.merge(n1, n2.next)
        return n2