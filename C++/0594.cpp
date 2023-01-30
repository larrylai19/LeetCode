class Solution {
public:
    int findLHS(vector<int>& nums) {
        int res = 0;
        map<int, int> m;
        for (auto& n : nums) {
            ++m[n];
        }
        
        for (auto it = next(m.begin()); it != m.end(); ++it) {
            auto pre = prev(it);
            if (it->first == pre->first + 1) {
                res = max(it->second + pre->second, res);
            }
        }

        return res;
    }
};
