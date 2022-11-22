class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        l = string.ascii_uppercase
        ret = ''
        
        while columnNumber:
            ret += l[columnNumber % 26 - 1]
            columnNumber = (columnNumber - 1) // 26
            
        return ret[::-1]