class Solution:
    def smallestSubsequence(self, s: str) -> str:
        cnt, visited = defaultdict(int), defaultdict(bool)
        for c in s:
            cnt[c] += 1
            
        ret = '0'
        for c in s:
            cnt[c] -= 1
            if visited[c]:
                continue
            visited[c] = True
            
            while c < ret[-1] and cnt[ret[-1]]:
                visited[ret[-1]] = False
                ret = ret[:-1]
            ret += c
            
        return ret[1:]