class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        '''
        greedy: 先讓全部人去 A，之後將到 B 的花費減去到 A 的花費做排序，前半部份的人去 B 會比較省，所以將花費加上該值
        '''
        
        ret = 0
        refund = []
        
        for l in costs:
            ret += l[0]
            refund.append(l[1] - l[0])
        refund.sort()
        
        return ret + sum(refund[:len(refund) // 2])