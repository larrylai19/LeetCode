class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ret = [[]]
        
        lastN, sz = nums[0], 1
        for n in nums:
            if n != lastN:
                lastN = n
                sz = len(ret)
            for i in range(len(ret) - sz, len(ret)):
                ret.append(ret[i].copy())
                ret[-1].append(n)

        return ret