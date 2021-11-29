class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        """return the length of the last word in the string"""
        return len(s.split()[-1])

