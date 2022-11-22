class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        if (len(keyName) < 3):
            return []
        
        dic = {}
        for i in range(len(keyName)):
            if keyName[i] not in dic:
                dic[keyName[i]] = []
            h = int(keyTime[i][:2])
            m = int(keyTime[i][3:])
            dic[keyName[i]].append(h * 60 + m)
            
        ret = []
        for n, t in dic.items():
            if len(t) < 3:
                continue
            
            t.sort()
            for i in range(2, len(t)):
                if t[i] - t[i-2] <= 60:
                    ret.append(n)
                    break
                    
        ret.sort()
        return ret