class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for c in s:
            stack.append(c)
            while len(stack) >= 2 and stack[-1] == stack[-2]:
                del stack[-2]
                del stack[-1]
        return ''.join(stack)