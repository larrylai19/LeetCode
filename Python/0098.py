# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root, -math.inf, math.inf)
        
    def dfs(self, root, mn, mx):
        if not root:
            return True
        
        if root.val <= mn or root.val >= mx:
            return False
        
        return self.dfs(root.left, mn, root.val) and self.dfs(root.right, root.val, mx)