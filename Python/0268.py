class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        ret = 0
        for i, n in enumerate(nums):
            ret ^= ((i + 1) ^ n)
        return ret