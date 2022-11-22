class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        rows = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']
        
        ret = []
        for w in words:
            if self.check(w, rows):
                ret.append(w)
        
        return ret
        
    def check(self, word, rows):
        word = word.lower()
        IDX = -1
        for ch in word:
            idx = -1
            for i, r in enumerate(rows):
                if ch in r:
                    idx = i
                    break
            if IDX != -1 and IDX != idx:
                return False
            IDX = idx
        return True