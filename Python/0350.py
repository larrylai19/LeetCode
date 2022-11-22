class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d1 = defaultdict(int)
        for i in nums1:
            d1[i] += 1
            
        d2 = defaultdict(int)
        for i in nums2:
            d2[i] += 1
        
        ret = []
        for k, v in d1.items():
            ret.extend([k] * min(v, d2[k]))

        return ret