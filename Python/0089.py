class Solution:
    def grayCode(self, n: int) -> List[int]:
        ret = [0]
        for i in range(n):
            sz = len(ret)
            for j in range(sz - 1, -1, -1):
                ret.append(ret[j] | (1 << i))
            print(ret)
        return ret