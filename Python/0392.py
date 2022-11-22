class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False
        
        i, j = 0, 0
        m, n = len(s), len(t)
        
        while i < len(s):
            while j < n and s[i] != t[j]:
                j += 1
            if j == n:
                return False
            
            i += 1
            j += 1
            
        return i == m