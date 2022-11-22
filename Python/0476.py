class Solution:
    def findComplement(self, num: int) -> int:
        ret = 1
        while ret <= num:
            ret <<= 1
        return (ret - 1) ^ num