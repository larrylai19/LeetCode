class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ret = 0
        stack = []
        heights.append(0) # 避免最後一塊板子沒被處理
        n = len(heights)
        
        for i in range(n):
            if not stack or heights[i] >= heights[stack[-1]]:
                stack.append(i)
            else:
                while stack and heights[i] <= heights[stack[-1]]:
                    h = heights[stack[-1]]
                    stack.pop()
                    w = i if not stack else i - stack[-1] - 1
                    ret = max(h * w, ret)
                stack.append(i)
        
        return ret
                