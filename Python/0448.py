class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        ret = []
        
        for n in nums:
            if nums[abs(n) - 1] > 0:
                nums[abs(n) - 1] *= -1
        
        for i, n in enumerate(nums):
            if n > 0:
                ret.append(i + 1)
        return ret