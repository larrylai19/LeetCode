class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ret = []
        self.dfs(n, k, [], 1, ret)
        return ret
        
    def dfs(self, n, k, l, s, ret):
        if len(l) == k:
            ret.append(l.copy())
            return
        
        for i in range(s, n + 1):
            l.append(i)
            self.dfs(n, k, l, i + 1, ret)
            l.pop()