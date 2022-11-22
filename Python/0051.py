class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        results = []
        queens = [['.'] * n for _ in range(n)]
        self.dfs(n, 0, queens, results)
        return results

    def dfs(self, n, currRow, queens, results):
        if currRow == n:
            results.append([''.join(i) for i in queens])
            return
        
        for i in range(n):
            if self.isValid(n, queens, currRow, i):
                queens[currRow][i] = 'Q'
                self.dfs(n, currRow + 1, queens, results)
                queens[currRow][i] = '.'

    def isValid(self, n, queens, row, col):
        """
        row, col: new queen's position
        """
        # check if queen on the same columns
        for i in range(row):
            if queens[i][col] == 'Q':
                return False
        
        # check if queen on left-top
        i, j = row - 1, col - 1
        while i >= 0 and j >= 0:
            if queens[i][j] == 'Q':
                return False
            i -= 1
            j -= 1
        
        # check if queen on right-top
        i, j = row - 1, col + 1
        while i >= 0 and j < n:
            if queens[i][j] == 'Q':
                return False
            i -= 1
            j += 1
        
        return True
