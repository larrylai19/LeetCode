# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.buildBST(0, len(nums) - 1, nums)
        
    def buildBST(self, l, r, nums):
        if l > r:
            return None
        m = (l + r) // 2
        return TreeNode(nums[m], self.buildBST(l, m - 1, nums), self.buildBST(m + 1, r, nums))