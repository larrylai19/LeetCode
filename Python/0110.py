# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        l = self.getDepth(root.left)
        r = self.getDepth(root.right)
        return abs(l - r) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)
        
    def getDepth(self, r):
        if not r:
            return 0      
        return max(self.getDepth(r.left), self.getDepth(r.right)) + 1
        