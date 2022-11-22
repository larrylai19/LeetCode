class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        dic = {}
        for i in range(26):
            dic[chr(i + 97)] = 0
        
        for c in dic:
            dic[c] = words[0].count(c)
        
        for w in words:
            for c in dic:
                dic[c] = min(w.count(c), dic[c])
        
        ret = []
        for a, b in dic.items():
            ret.extend([a] * b)
            
        return ret