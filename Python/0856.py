class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        ret = 0
        stack = []
        
        for c in s:
            if c == '(':
                stack.append(ret)
                ret = 0
            else:
                ret = stack.pop() + max(2 * ret, 1)
        
        return ret