class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        n = len(nums) // 2
        for val, times in Counter(nums).items():
            if times == n:
                return val