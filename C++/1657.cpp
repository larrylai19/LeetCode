class Solution {
public:
    bool closeStrings(string word1, string word2) {
        if (word1.size() != word2.size()) {
            return false;
        }

        vector<int> charSet1(128), charSet2(128);
        vector<int> charCount1(128), charCount2(128);

        for (const auto& ch : word1) {
            charSet1[ch] = 1;
            ++charCount1[ch];
        }
        for (const auto& ch : word2) {
            charSet2[ch] = 1;
            ++charCount2[ch];
        }

        if (charSet1 != charSet2) {
            return false;
        }

        sort(charCount1.begin(), charCount1.end());
        sort(charCount2.begin(), charCount2.end());

        return charCount1 == charCount2;
    }
};
