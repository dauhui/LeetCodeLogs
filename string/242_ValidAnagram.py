from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """return true if t is an anagram of s"""
        return Counter(s) == Counter(t)

