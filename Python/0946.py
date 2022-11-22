class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        
        for n in pushed:
            stack.append(n)
            while stack and stack[-1] == popped[0]:
                stack.pop()
                popped.pop(0)
        
        return not stack and not popped