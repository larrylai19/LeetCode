class Solution {
public:
    int totalNQueens(int n) {
        vector<vector<string>> results;
        vector<string> queens(n, string(n, '.'));
        dfs(n, 0, queens, results);
        return results.size();
    }

    
    void dfs(int n, int currRow, vector<string>& queens, vector<vector<string>>& results) {
        if (currRow == n) {
            results.push_back(queens);
            return;
        }

        for (int i = 0; i < n; ++i) {
            if (isValid(n, queens, currRow, i)) {
                queens[currRow][i] = 'Q';
                dfs(n, currRow + 1, queens, results);
                queens[currRow][i] = '.';
            }
        }
    }

    // row, col: new queen's position
    bool isValid(int n, vector<string>& queens, int row, int col) {
        // check if queen on the same columns
        for (int i = 0; i < row; ++i) {
            if (queens[i][col] == 'Q') {
                return false;
            }
        }
        
        // check if queen on left-top
        for (int i = row - 1, j = col - 1; i >= 0 && j >= 0; --i, --j) {
            if (queens[i][j] == 'Q') {
                return false;
            }
        }
        
        // check if queen on right-top
        for (int i = row - 1, j = col + 1; i >= 0 && j < n; --i, ++j) {
            if (queens[i][j] == 'Q') {
                return false;
            }
        }

        return true;
    }
};
