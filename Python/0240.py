class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if target < matrix[0][0] or target > matrix[-1][-1]:
            return False
        
        x, y = len(matrix) - 1, 0
        while True:
            if matrix[x][y] > target:
                x -= 1
            elif matrix[x][y] < target:
                y += 1
            else:
                return True
            
            if x < 0 or y >= len(matrix[0]):
                break
            
        return False