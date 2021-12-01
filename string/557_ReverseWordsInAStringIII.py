class Solution:
    def reverseWords(self, s: str) -> str:
        """reverse the order of characters in each word within a sentence"""
        return " ".join(map(lambda x: "".join(list(reversed(x))), s.split()))
