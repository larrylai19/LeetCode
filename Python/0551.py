class Solution:
    def checkRecord(self, s: str) -> bool:
        late = 0
        absent = 0
        for ch in s:
            if ch == 'A':
                absent += 1
                late = 0
            elif ch == 'L':
                late += 1
            elif ch == 'P':
                late = 0
            
            if absent > 1 or late >= 3:
                return False
        return True