# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        return self.build(head, None)
        
    def build(self, head, tail):
        if head == tail:
            return None
        
        slow, fast = head, head
        while fast != tail and fast.next != tail:
            slow = slow.next
            fast = fast.next.next
        
        return TreeNode(slow.val,
                        self.build(head, slow),
                        self.build(slow.next, tail))