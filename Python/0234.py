# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        s = ''
        curr = head
        while curr:
            s += str(curr.val)
            curr = curr.next
        return s[::-1] == s
            