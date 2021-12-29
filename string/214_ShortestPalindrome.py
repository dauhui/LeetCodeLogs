class Solution:
    def shortestPalindrome(self, s: str) -> str:
        """
        put "in front of" the string to make palindrome
        
        ref from sol
        aacecaaa ->    aaacecaa - x
                    (a)aacecaa  - v
        """
        r = s[::-1]
        for i in range(len(r) + 1):
            if s.startswith(r[i:]):
                return r[:i] + s

