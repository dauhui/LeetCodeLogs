class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        """
        find the extra chracter
        
        - take ord
        - take xor
        - take chr
        """        
        extra = 0
        
        for c in s: extra ^= ord(c)
        for c in t: extra ^= ord(c)
        
        return chr(extra)

