class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        stack<int64_t> stack;
        set<string> operands = {"+", "-", "*", "/"};

        for (const auto& ch : tokens) {
            if (!operands.count(ch)) {
                stack.push(stoi(ch));
            } else {
                int64_t second = stack.top();
                stack.pop();
                int64_t first = stack.top();
                stack.pop();

                switch (ch[0]) {
                    case '+':
                        stack.push(first + second);
                        break;
                    case '-':
                        stack.push(first - second);
                        break;
                    case '*':
                        stack.push(first * second);
                        break;
                    case '/':
                        stack.push(first / second);
                        break;
                }
            }
        }

        return stack.top();
    }
};
