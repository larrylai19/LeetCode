class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        result = ''
        numbers = [str(i) for i in range(1, 11)]
        
        factorial = [1] * n
        for i in range(2, len(factorial)):
            factorial[i] = i * factorial[i - 1]
        
        # for index
        k -= 1
        for i in range(n, 0, -1):
            j = k // factorial[i - 1]
            k %= factorial[i - 1]
            result += numbers[j]
            del numbers[j]

        return result
