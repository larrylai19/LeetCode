"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        self.mx = 0
        self.dfs(root, 1)
        return self.mx
        
    def dfs(self, node, curDept):
        if not node:
            return
        
        self.mx = max(curDept, self.mx)
        for n in node.children:
            self.dfs(n, curDept + 1)