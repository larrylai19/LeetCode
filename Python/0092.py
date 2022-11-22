# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    '''
    1 2 3 4 5
    1 3 2 4 5
    1 4 3 2 5
    pre = 1
    '''    
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        
        pre = dummy
        for i in range(left - 1):
            pre = pre.next
        
        cur = pre.next
        for i in range(left, right):
            tmp = cur.next
            cur.next = tmp.next
            tmp.next = pre.next
            pre.next = tmp

        return dummy.next