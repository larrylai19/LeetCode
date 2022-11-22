# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ''
        
        ret = str(root.val)
        if not root.left and not root.right:
            return ret
        
        ret += f'({self.tree2str(root.left)})'
        
        if root.right:
            ret += f'({self.tree2str(root.right)})'
            
        return ret