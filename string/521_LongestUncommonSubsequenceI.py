class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        """
        - an uncommon subsequence is a string that is subsequence of one but of the other
            - a longer string is definitely the longest uncommon subsequence
            - same length
                1. different string
                2. the same string
        """
        return -1 if a == b else max(len(a), len(b))

