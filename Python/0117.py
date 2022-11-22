"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        
        p = root.next
        while p and not p.left and not p.right:
            p = p.next
        if p:
            p = p.left if p.left else p.right
        
        if root.right:
            root.right.next = p
        if root.left:
            root.left.next = root.right if root.right else p

        self.connect(root.right)
        self.connect(root.left)
        
        return root