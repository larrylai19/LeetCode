# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.sum = 0
        self.dfs(root, low, high)
        return self.sum
        
    def dfs(self, node, low, high):
        if not node:
            return
        if node.val >= low and node.val <= high:
            self.sum += node.val
        self.dfs(node.left, low, high)
        self.dfs(node.right, low, high)