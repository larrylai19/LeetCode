# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ret = []
        self.dfs(root, [], ret)
        return ['->'.join(list(map(str, i))) for i in ret]
        
    def dfs(self, r, l, ret):
        if not r:
            return
        if not r.left and not r.right:
            ret.append(l + [r.val])
        self.dfs(r.left, l + [r.val], ret)
        self.dfs(r.right, l + [r.val], ret)