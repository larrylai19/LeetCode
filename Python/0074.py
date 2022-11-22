class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = self.findRow(0, len(matrix) - 1, target, matrix)
        if row == -1:
            return False
        return self.findTargetInARow(row, 0, len(matrix[row]) - 1, target, matrix)
    
    def findTargetInARow(self, row, l, r, target, matrix):
        if l >= r:
            return matrix[row][l] == target
        
        m = (l + r) // 2
        if matrix[row][m] == target:
            return True
        if target > matrix[row][m]:
            return self.findTargetInARow(row, m + 1, r, target, matrix)
        return self.findTargetInARow(row, l, m, target, matrix)
        
    def findRow(self, up, down, target, matrix):
        if up >= down:
            return up if target >= matrix[up][0] and target <= matrix[up][-1] else -1
        
        m = (up + down) // 2
        if target >= matrix[m][0] and target <= matrix[m][-1]:
            return m
        
        if target < matrix[m][0]:
            return self.findRow(up, m, target, matrix)
        return self.findRow(m + 1, down, target, matrix)