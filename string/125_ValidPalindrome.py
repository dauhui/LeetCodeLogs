class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        return true if it is a palindrome, or false otherwise
    
    
        - start from both side
        - check one-by-one
        - skip if not numerics or alphabatics
        """

        l, r = 0, len(s) - 1

        while l < r:

            while l < len(s) - 1 and not s[l].isalpha() and not s[l].isnumeric(): l += 1
            while r > 0 and not s[r].isalpha() and not s[r].isnumeric(): r -= 1

            if l < r and s[l].lower() != s[r].lower(): return False
            
            l += 1
            r -= 1
        
        return True
