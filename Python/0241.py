class Solution:
    def __init__(self):
        self.memo = {}
    
    def diffWaysToCompute(self, expression: str) -> List[int]:
        if expression in self.memo:
            return self.memo[expression]
        
        ret = []
        exps = ['+', '-', '*']
        
        for i, exp in enumerate(expression):
            if exp in exps:
                left = self.diffWaysToCompute(expression[:i])
                right = self.diffWaysToCompute(expression[i+1:])
                
                for x in left:
                    for y in right:
                        ret.append(eval(f'{x}{exp}{y}'))
        
        if not ret:
            ret.append(int(expression))
            
        self.memo[expression] = ret
        return ret