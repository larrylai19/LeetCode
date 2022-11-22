"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        l = []
        self.post(root, l)
        return l
        
    def post(self, n, l):
        if not n:
            return
        for n1 in n.children:
            self.post(n1, l)
        l.append(n.val)