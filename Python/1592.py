class Solution:
    def reorderSpaces(self, text: str) -> str:
        spaceNum = text.count(' ')
        lst = text.split()
        if len(lst) == 1:
            return lst[0] + ' ' * spaceNum
        each = spaceNum // (len(lst) - 1)
        ret = (' ' * each).join(lst)
        return ret + ' ' * (spaceNum % (len(lst) - 1))