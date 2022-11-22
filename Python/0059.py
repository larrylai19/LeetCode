class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ret = [[0] * n for _ in range(n)]
        up, down = 0, n - 1
        left, right = 0, n - 1
        val = 1
        
        while True:
            for i in range(left, right + 1):
                ret[up][i] = val
                val += 1
            up += 1
            if up > down:
                break
            
            for i in range(up, down + 1):
                ret[i][right] = val
                val += 1
            right -= 1
            if right < left:
                break
                
            for i in range(right, left - 1, -1):
                ret[down][i] = val
                val += 1
            down -= 1
            if down < up:
                break
            
            for i in range(down, up - 1, -1):
                ret[i][left] = val
                val += 1
            left += 1
            if left > right:
                break
        
        return ret