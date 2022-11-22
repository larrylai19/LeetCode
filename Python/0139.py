class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        Dict = set(wordDict)
        dp = [True] + [False] * len(s)
        s = ' ' + s
        
        for i in range(1, len(s)):
            for j in range(i):
                dp[i] |= dp[j] and s[j+1:i+1] in Dict

        return dp[-1]