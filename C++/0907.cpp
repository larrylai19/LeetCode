class Solution {
public:
    int sumSubarrayMins(vector<int>& arr) {
        int result = 0, M = 1e9 + 7;
        stack<int> st{{-1}};
        vector<int> dp(arr.size() + 1);
        
        for (int i = 0; i < arr.size(); ++i) {
            // from last to first find first number less than current number
            while (st.top() != -1 && arr[i] <= arr[st.top()]) {
                st.pop();
            }

            dp[i + 1] = (dp[st.top() + 1] + (i - st.top()) * arr[i]) % M;
            st.push(i);
            result = (result + dp[i + 1]) % M;
        }

        return result;
    }
};
