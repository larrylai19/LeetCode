class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operands = ['+', '-', '*', '/']
        for token in tokens:
            if token not in operands:
                stack.append(int(token))
            else:
                temp = int(eval(f'{stack[-2]}{token}{stack[-1]}'))
                del stack[-2:]
                stack.append(temp)
        return stack[-1]
