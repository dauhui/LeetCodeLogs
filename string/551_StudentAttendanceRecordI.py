class Solution:
    def checkRecord(self, s: str) -> bool:
        """
        award if <2 absent AND late for <3 consecutive lates
        """
        
        absent, consecutiveLate = 0, 0
        for c in s:
            consecutiveLate = consecutiveLate + 1 if c == 'L' else 0
            absent = absent + 1 if c == 'A' else absent
            if consecutiveLate >= 3 or absent >= 2: return False
        return True

