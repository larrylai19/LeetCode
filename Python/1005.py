import heapq

class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        for i in range(k):
            n = heapq.heappop(nums)
            heapq.heappush(nums, -n)
        return sum(nums)