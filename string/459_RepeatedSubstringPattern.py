class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        """
        a better way from sol:
        
            - assume string has repeated substring, so the string will be 
                => s = S..S
            - let's repeat it again and get 
                => s + s = S..S S..S
            - we can remove the first and last characters
                => X..S S..Y
                => if s has repeated substring, the backup repeat unit can restore s
        """
        
        return s in (s+s)[1:-1]

