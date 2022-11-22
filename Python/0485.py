class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ret, cur = 0, 0
        for n in nums:
            if n == 1:
                cur += 1
            else:
                ret = max(ret, cur)
                cur = 0
        return max(cur, ret)