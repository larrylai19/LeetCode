# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        while head:
            tmp = head.next
            cur = dummy
            while cur.next and cur.next.val <= head.val:
                cur = cur.next
            head.next = cur.next
            cur.next = head
            head = tmp
        return dummy.next