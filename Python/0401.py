class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        ret = []
        
        for i in range(12):
            for j in range(60):
                if bin(i).count('1') + bin(j).count('1') == turnedOn:
                    ret.append(f'{str(i)}:{str(j):0>2}')
        
        return ret