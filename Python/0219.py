class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        pos = {}
        for i, n in enumerate(nums):
            if n in pos and i - pos[n] <= k:
                return True
            pos[n] = i
        return False