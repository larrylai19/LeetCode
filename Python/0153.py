class Solution:
    def findMin(self, nums: List[int]) -> int:
        return self.DnC(0, len(nums) - 1, nums)
        
    def DnC(self, l, r, nums):
        if nums[l] < nums[r] or l == r:
            return nums[l]
        m = (l + r) // 2
        return min(self.DnC(l, m, nums), self.DnC(m + 1, r, nums))