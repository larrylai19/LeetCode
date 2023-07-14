class Solution {
public:
    int longestSubsequence(vector<int>& arr, int difference) {
        int mx = 1;
        unordered_map<int, int> dp;
        for (const auto& n : arr) {
            dp[n] = dp[n - difference] + 1;
            mx = max(dp[n], mx);
        }
        return mx;
    }
};
