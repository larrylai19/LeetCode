class Solution {
public:
    int hIndex(vector<int>& citations) {
        int maxHIndex = 0;
        int n = citations.size();
        int left = 0, right = n;

        while (left < right) {
            int mid = (left + right) / 2;
            int h = citations[mid];
            int atLeastHCount = n - mid;
            maxHIndex = max(maxHIndex, min(h, atLeastHCount));

            if (h < atLeastHCount) {
                left = mid + 1;
            } else if (h > atLeastHCount) {
                right = mid;
            } else {
                break;
            }
        }

        return maxHIndex;
    }
};
