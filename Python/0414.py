class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        mx = [nums[0], None, None]
        for n in nums[1:]:
            if n in mx:
                continue
            if n > mx[0]:
                mx = [n] + mx[:2]
            elif not mx[1] or n > mx[1]:
                mx[1:] = [n, mx[1]]
            elif not mx[2] or n > mx[2]:
                mx[2] = n
        return mx[2] if mx[2] != None else mx[0]