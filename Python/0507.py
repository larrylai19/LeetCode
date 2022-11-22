class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num == 1:
            return False
        ret = 1
        for i in range(2, int(sqrt(num)) + 1):
            if num % i == 0:
                ret += i + num // i
        return ret == num