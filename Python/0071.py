class Solution:
    def simplifyPath(self, path: str) -> str:
        l = [s for s in path.split('/') if s]
        stack = []
        
        for s in l:
            if s == '..':
                if stack:
                    stack.pop()
            elif s != '.':
                stack.append(s)

        return '/' + '/'.join(stack)