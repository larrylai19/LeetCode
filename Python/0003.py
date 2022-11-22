class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = defaultdict(lambda: -1)
        
        l, maxL = 0, 0
        for r, c in enumerate(s):
            l = max(l, d[c] + 1)
            maxL = max(r - l + 1, maxL)
            d[c] = r

        return maxL