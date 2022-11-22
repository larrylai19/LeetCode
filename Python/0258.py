class Solution:
    def addDigits(self, num: int) -> int:
        if num < 10:
            return num
        ret = 0
        while num > 0:
            ret += num % 10
            num //= 10
        return self.addDigits(ret)