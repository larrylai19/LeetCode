class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        l = []
        for i, ch in enumerate(s):
            if ch == c:
                l.append(0)
                continue
            lth = float('inf')
            le, r = i - 1, i + 1
            while le >= 0:
                if s[le] == c:
                    lth = min(lth, i - le)
                    break
                le -= 1
            while r < len(s):
                if s[r] == c:
                    lth = min(lth, r - i)
                    break
                r += 1
            l.append(lth)            
        return l