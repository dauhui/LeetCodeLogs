class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        """
        return true if the usage of capitals is correct

        1. first capital:
            -> rest are small
            -> rest are capital
        2. first small
            -> rest are small
            
        (a) check one-by-one manually
        (b) one-liner solution: compare sting
            -> lower
            -> upper
            -> capitalize
        """

        if len(word) == 1: return True
        
        if word[0].isupper() and word[1].isupper():
            for i in range(2, len(word)): 
                if not word[i].isupper(): return False               
        else:
            for i in range(1, len(word)):
                if word[i].isupper(): return False
                
        return True
