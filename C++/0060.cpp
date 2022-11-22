class Solution {
public:
    string getPermutation(int n, int k) {
        string result = "";
        string numbers = "123456789";

        vector<int> factorial(n, 1);
        for (int i = 2; i < n; ++i) {
            factorial[i] = i * factorial[i - 1];
        }

        --k; // for index
        for (int i = n; i >= 1; --i) {
            int j = k / factorial[i - 1];
            k %= factorial[i - 1];
            result += numbers[j];
            numbers.erase(j, 1);
        }

        return result;
    }
};
