class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        lst = []
        for i in mat:
            lst.extend(i)
        if len(lst) != r * c:
            return mat
        return [lst[i:i+c] for i in range(0, len(lst), c)]