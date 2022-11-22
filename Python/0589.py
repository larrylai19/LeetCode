"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        l = []
        self.pre(root, l)
        return l
        
    def pre(self, n, l):
        if not n:
            return
        l.append(n.val)
        for n1 in n.children:
            self.pre(n1, l)