class Solution {
public:
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        map<int, vector<int>> preReq;
        vector<int> numPreReq(numCourses);
        for (const auto& v : prerequisites) {
            ++numPreReq[v[0]];
            preReq[v[1]].push_back(v[0]);
        }

        queue<int> courses;
        for (int i = 0; i < numCourses; ++i) {
            if (numPreReq[i] == 0) {
                courses.push(i);
            }
        }

        while (!courses.empty()) {
            int cur = courses.front();
            courses.pop();

            for (const auto& course : preReq[cur]) {
                --numPreReq[course];
                if (!numPreReq[course]) {
                    courses.push(course);
                }
            }
        }

        for (int i = 0; i < numCourses; ++i) {
            if (numPreReq[i]) {
                return false;
            }
        }

        return true;
    }
};
