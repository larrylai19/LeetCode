class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        l = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        dic = {}
        for i in range(26):
            dic[chr(i + 97)] = l[i]
        
        s = set()
        for w in words:
            s.add(''.join([dic[i] for i in w]))
        
        return len(s)