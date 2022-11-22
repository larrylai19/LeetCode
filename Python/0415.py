class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        if int(num1) > int(num2):
            ret = list(reversed(list(map(int, num1))))
            other = list(reversed(list(map(int, num2))))
        else:
            ret = list(reversed(list(map(int, num2))))
            other = list(reversed(list(map(int, num1))))
        ret.append(0)
        for i in range(len(other)):
            ret[i] += other[i]
        
        for i in range(len(ret) - 1):
            ret[i + 1] += ret[i] // 10
            ret[i] %= 10
        
        if ret[-1] == 0:
            del ret[-1]
        ret.reverse()
        ret = ''.join(list(map(str, ret)))
        return ret