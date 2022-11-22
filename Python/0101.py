# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.isSymmertric(root, root)
        
    def isSymmertric(self, left, right):
        if not left or not right:
            return left == right
        return left.val == right.val and \
                self.isSymmertric(left.left, right.right) and \
                self.isSymmertric(left.right, right.left)