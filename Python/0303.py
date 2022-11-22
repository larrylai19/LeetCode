class NumArray:

    def __init__(self, nums: List[int]):
        self.sum = nums.copy()
        for i in range(1, len(self.sum)):
            self.sum[i] += self.sum[i-1]
        self.sum = [0] + self.sum

    def sumRange(self, left: int, right: int) -> int:
        return self.sum[right + 1] - self.sum[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)