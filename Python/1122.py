class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        dic = {}
        for i, n in enumerate(arr2):
            dic[n] = i
        for n in arr1:
            if n not in dic:
                dic[n] = 10000 + n
        return sorted(arr1, key=lambda x: dic[x])