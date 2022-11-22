class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur, ret = nums[0], nums[0]
        for n in nums[1:]:
            cur = max(n, cur + n)
            ret = max(cur, ret)
        return ret