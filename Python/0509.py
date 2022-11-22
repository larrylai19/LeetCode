class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        
        n1, n2 = 0, 1
        for i in range(n - 1):
            tmp = n1 + n2
            n1, n2 = n2, tmp
        
        return n2