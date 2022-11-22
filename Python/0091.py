class Solution:
    def numDecodings(self, s: str) -> int:
        idx = 0
        while idx < len(s) and s[idx] == '0':
            idx += 1
        s = s[idx:]
        
        dp = [1] * 2 + [0] * len(s)
        
        for i in range(len(s)):
            j = i + 2
            
            if int(s[i]) > 0 and int(s[i]) < 10:
                dp[j] += dp[j-1]
            
            if i > 0:
                twoDigit = int(s[i-1:i+1])
                if twoDigit >= 10 and twoDigit <= 26:
                    dp[j] += dp[j-2]
        
        return dp[-1] if idx == 0 else 0