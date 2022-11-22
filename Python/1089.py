class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        idx = 0
        orgLenth = len(arr)
        while idx < orgLenth:
            if arr[idx] == 0:
                arr.insert(idx, 0)
                idx += 1
            idx += 1
        for i in range(len(arr) - orgLenth):
            del arr[-1]