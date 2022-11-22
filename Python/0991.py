class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        ret = 0
        
        while target > startValue:
            target = target // 2 if target % 2 == 0 else target + 1
            ret += 1
        
        return ret + startValue - target