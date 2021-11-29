class Solution:
    def countSegments(self, s: str) -> int:
        """return the number of space-saparated segments in the string"""
        return len(s.split())
