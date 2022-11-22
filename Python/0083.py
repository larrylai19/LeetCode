# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p = head
        while p and p.next:
            tmp = p.next
            while tmp and p.val == tmp.val:
                tmp = tmp.next
            p.next = tmp
            p = p.next
        return head