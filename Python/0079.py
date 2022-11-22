class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        
        for i in range(m):
            for j in range(n):
                if self.dfs(board, word, 0, i, j):
                    return True
                
        return False
        
    def dfs(self, board, word, idx, i, j):
        if idx == len(word):
            return True
        
        if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or board[i][j] != word[idx]:
            return False
        
        c = board[i][j]
        board[i][j] = '#'
        ret = self.dfs(board, word, idx + 1, i, j + 1) or \
                self.dfs(board, word, idx + 1, i, j - 1) or \
                self.dfs(board, word, idx + 1, i + 1, j) or \
                self.dfs(board, word, idx + 1, i - 1, j)
        board[i][j] = c
        return ret