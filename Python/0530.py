# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        lst = []
        self.inorder(root, lst)
        ret = float('inf')
        for i in range(len(lst) - 1):
            ret = min(ret, lst[i+1] - lst[i])
        return ret
    
    def inorder(self, node, lst):
        if not node:
            return
        self.inorder(node.left, lst)
        lst.append(node.val)
        self.inorder(node.right, lst)
        