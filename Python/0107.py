# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        ret = []
        self.inorder(root, 0, ret)
        return ret[::-1]
        
    def inorder(self, r, deep, ret):
        if not r:
            return
        
        self.inorder(r.left, deep + 1, ret)
        if len(ret) <= deep:
            ret.extend([] for _ in range(deep - len(ret) + 1))
        ret[deep].append(r.val)
        self.inorder(r.right, deep + 1, ret)