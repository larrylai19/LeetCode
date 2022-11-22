class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        ret = []
        sp = text.split()
        if len(sp) < 3:
            return ret
        for i in range(2, len(sp)):
            if sp[i-2] == first and sp[i-1] == second:
                ret.append(sp[i])
        return ret