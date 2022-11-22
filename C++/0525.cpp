class Solution {
public:
    int findMaxLength(vector<int>& nums) {
        int sum = 0, maxLen = 0;
        unordered_map<int, int> m;
        m[0] = -1;
        
        for (int i = 0; i < nums.size(); ++i) {
            sum += nums[i] ? 1 : -1;
            
            if (m.count(sum)) maxLen = max(i - m[sum], maxLen);
            else m[sum] = i;
        }
        
        return maxLen;
    }
};