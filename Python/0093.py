class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ret = []
        self.dfs(s, 0, [], ret)
        return ret
        
    def dfs(self, s, idx, curr_address, ret):
        if idx == len(s):
            if len(curr_address) == 4:
                ret.append('.'.join(curr_address))
            return
        
        for i in range(idx, min(idx + 3, len(s))):
            address = s[idx:i+1]
            if i == idx:
                self.dfs(s, i + 1, curr_address + [address], ret)
            elif address[0] != '0':
                if int(address) <= 255:
                    self.dfs(s, i + 1, curr_address + [address], ret)