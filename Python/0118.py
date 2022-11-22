class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ret = [[1]]
        
        for i in range(1, numRows):
            l = []
            for j in range(i + 1):
                if j == 0 or j == i:
                    l.append(1)
                else:
                    l.append(ret[i-1][j-1] + ret[i-1][j])
            ret.append(l)
        
        return ret