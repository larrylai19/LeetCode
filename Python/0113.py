# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ret = []
        self.dfs(root, [], 0, targetSum, ret)
        return ret
        
    def dfs(self, root, lst, currSum, targetSum, ret):
        if not root:
            return

        currSum += root.val
        if currSum == targetSum and not root.left and not root.right:
            ret.append(lst + [root.val])
            
        self.dfs(root.left, lst + [root.val], currSum, targetSum, ret)
        self.dfs(root.right, lst + [root.val], currSum, targetSum, ret)