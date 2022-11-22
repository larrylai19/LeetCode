class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return '0'
        
        isNegative = True if num < 0 else False
        num = abs(num)
        ret = []
        
        while num > 0:
            ret.append(str(num % 7))
            num //= 7
        
        ret.reverse()
        return '-' + ''.join(ret) if isNegative else ''.join(ret)