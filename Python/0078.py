class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ret = [[]]

        for i in nums:
            for j in range(len(ret)):
                ret.append(ret[j].copy())
                ret[-1].append(i)

        return ret