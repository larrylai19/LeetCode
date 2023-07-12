class Solution {
private:
    map<int, bool> isSafeNode;

    // return true if node idx is a safe node
    bool dfs(int idx, set<int>& traveled, vector<vector<int>>& graph) {
        if (isSafeNode.count(idx)) {
            return isSafeNode[idx];
        }

        bool isSafe = true;
        traveled.insert(idx);

        if (!graph[idx].empty()) {
            for (const auto& nextNode : graph[idx]) {
                // if there have any loops,
                // this node must not be a safe node
                if (traveled.count(nextNode) ||
                        !dfs(nextNode, traveled, graph)) {
                    isSafe = false;
                    break;
                }
            }
        }

        traveled.erase(idx);
        isSafeNode[idx] = isSafe;
        return isSafe;
    }

public:
    vector<int> eventualSafeNodes(vector<vector<int>>& graph) {
        vector<int> safeNodes;
        set<int> traveled;
        for (int i = 0; i < graph.size(); ++i) {
            if (dfs(i, traveled, graph)) {
                safeNodes.push_back(i);
            }
        }
        return safeNodes;
    }
};
