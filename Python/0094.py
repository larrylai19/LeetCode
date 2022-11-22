# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ret = []
        self.dfs(root, ret)
        return ret
        
    def dfs(self, r, lst):
        if not r:
            return
        
        self.dfs(r.left, lst)
        lst.append(r.val)
        self.dfs(r.right, lst)