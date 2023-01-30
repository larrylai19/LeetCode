class Solution {
public:
    int maxCount(int m, int n, vector<vector<int>>& ops) {
        int mn[2] = {m, n};
        for (auto& op : ops) {
            mn[0] = min(mn[0], op[0]);
            mn[1] = min(mn[1], op[1]);
        }
        return mn[0] * mn[1];
    }
};
