class Solution:
    def reverseWords(self, s: str) -> str:
        """reverse the order of the words"""
        return " ".join(reversed(s.split()))
