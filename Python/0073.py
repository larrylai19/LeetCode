# ref: https://www.cnblogs.com/grandyang/p/4341590.html

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # need with O(1) space complexity
        
        flag = [False] * 2
        
        m, n = len(matrix), len(matrix[0])
        
        for i in range(m):
            if matrix[i][0] == 0:
                flag[0] = True    
                
        for j in range(n):
            if matrix[0][j] == 0:
                flag[1] = True
        
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
                    
        for i in range(1, m):
            for j in range(1, n):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0
                    
        if flag[0]:
            for i in range(m):
                matrix[i][0] = 0
                
        if flag[1]:
            for j in range(n):
                matrix[0][j] = 0