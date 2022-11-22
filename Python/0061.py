# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 0 or not head:
            return head
        
        n = 1
        last = head
        while last.next:
            last = last.next
            n += 1
        last.next = head
        
        k %= n
        last = head
        for i in range(n - k - 1):
            last = last.next
            
        head = last.next
        last.next = None
               
        return head