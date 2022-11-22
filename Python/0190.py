class Solution:
    def reverseBits(self, n: int) -> int:
        binStr = bin(n)[2:][::-1]
        if len(binStr) < 32:
            binStr += '0' * (32 - len(binStr))
        return int(binStr, 2)