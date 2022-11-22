"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        
        newHead = Node(head.val)
        nodeNum = {head: newHead}
        
        p1, p2 = newHead, head.next
        while p2:
            p1.next = Node(p2.val)
            nodeNum[p2] = p1.next
            p1, p2 = p1.next, p2.next
        
        p1, p2 = newHead, head
        while p2:
            if p2.random in nodeNum:
                p1.random = nodeNum[p2.random]
            p1, p2 = p1.next, p2.next
        
        return newHead
        
        