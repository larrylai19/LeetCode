# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1, n2 = l1, l2
        
        while n1 and n2:
            n1.val += n2.val
            if not n1.next:
                n1.next = n2.next
                break
            n1, n2 = n1.next, n2.next

        carry = 0
        n1 = l1
        while n1:
            n1.val += carry
            carry = n1.val // 10
            n1.val %= 10
            if not n1.next and carry:
                n1.next = ListNode(carry)
                break
            n1 = n1.next

        return l1