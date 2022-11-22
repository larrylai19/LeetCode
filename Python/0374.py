# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l, r = 1, n
        while True:
            m = (l + r) // 2
            ret = guess(m)
            if ret == 0:
                break
            elif ret == 1:
                l = m + 1
            else:
                r = m
        return m