class Solution {
public:
    vector<vector<int>> findWinners(vector<vector<int>>& matches) {
        map<int, int> m;
        for (auto& v : matches) {
            m[v[0]] += 0;
            ++m[v[1]];
        }

        vector<int> allWin, loseOne;
        for (auto& [player, loseTimes] : m) {
            if (loseTimes == 0) {
                allWin.push_back(player);
            } else if (loseTimes == 1) {
                loseOne.push_back(player);
            }
        }
        
        return {allWin, loseOne};
    }
};
