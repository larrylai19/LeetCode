# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.prev, self.first, self.second = [None] * 3
        self.inorder(root)
        self.first.val, self.second.val = self.second.val, self.first.val
        
        
    def inorder(self, root):
        if not root:
            return
        self.inorder(root.left)
        if not self.prev:
            self.prev = root
        if self.prev.val > root.val:
            if not self.first:
                self.first = self.prev
            self.second = root
        self.prev = root
        self.inorder(root.right)