# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ret = []
        self.postorder(root, ret)
        return ret
        
    def postorder(self, r, ret):
        if not r:
            return
        
        self.postorder(r.left, ret)
        self.postorder(r.right, ret)
        ret.append(r.val)