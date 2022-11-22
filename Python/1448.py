# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return self.dfs(root, -1e6)
        
    def dfs(self, node, curr_max):
        if not node:
            return 0
        return self.dfs(node.left, max(curr_max, node.val)) + \
                self.dfs(node.right, max(curr_max, node.val)) + \
                (1 if node.val >= curr_max else 0)
    