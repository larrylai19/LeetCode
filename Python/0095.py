# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        return self.DnC(1, n)
        
    def DnC(self, l, r):
        if l > r:
            return [None]
        ret = []
        for i in range(l, r + 1):
            ln = self.DnC(l, i - 1)
            rn = self.DnC(i + 1, r)
            for L in ln:
                for R in rn:
                    ret.append(TreeNode(i, L, R))
        return ret

#     def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
#         return self.DnC(1, n + 1)
        
#     def DnC(self, l, r):
#         if l > r:
#             return [None]
        
#         ret = []
#         # i 做為 root
#         for i in range(l, r):
#             left, right = self.DnC(l, i), self.DnC(i + 1, r)
#             for ln in left:
#                 for rn in right:
#                     ret.append(TreeNode(i, ln, rn))
                     
#         return ret