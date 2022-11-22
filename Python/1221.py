class Solution:
    def balancedStringSplit(self, s: str) -> int:
        l, r = 0, 0
        ret = 0
        
        for c in s:
            if c == 'L':
                l += 1
            else:
                r += 1
            
            if l == r:
                ret += 1
                l, r = 0, 0
            
        return ret