# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        dummy = ListNode(0, head)
        p = dummy
        while p and p.next and p.next.next:
            if p.next.val == p.next.next.val:
                tmp = p.next.next
                while tmp and tmp.val == p.next.val:
                    tmp = tmp.next
                p.next = tmp
            else:
                p = p.next
        return dummy.next