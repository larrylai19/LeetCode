// fast IO
static auto __ = []() 
{
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(nullptr);
    std::cout.tie(nullptr);
    return 0;
}();
class Solution {
public:
    int minDistance(string word1, string word2) {
        int l1 = word1.size(), l2 = word2.size();
        auto dp = vector<vector<int>>(l1 + 1, vector<int>(l2 + 1));
        for(int i = 0; i <= l1; ++i)
            dp[i][0] = i;
        for(int j = 0; j <= l2; ++j)
            dp[0][j] = j;
        for(int i = 1; i <= l1; ++i)
            for(int j = 1; j <= l2; ++j)
                if(word1[i - 1] == word2[j - 1])
                    dp[i][j] = dp[i - 1][j - 1];
                else
                    dp[i][j] = 1 + min(dp[i - 1][j], min(dp[i][j - 1], dp[i - 1][j - 1]));
        return dp[l1][l2];
    }
};