class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        keys = ''.join(s.split('-')).upper()
        lst = []
        for i in range(len(keys), 0, -k):
            lst.append(keys[max(0, i - k):i])
        lst.reverse()
        return '-'.join(lst)