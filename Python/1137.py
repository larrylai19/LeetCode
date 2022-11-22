class Solution:
    def tribonacci(self, n: int) -> int:
        if n < 2:
            return n
        
        first = 0
        second = 1
        third = 1
        for i in range(n - 2):
            tmp = first
            first = second
            second = third
            third = tmp + first + second
        
        return third