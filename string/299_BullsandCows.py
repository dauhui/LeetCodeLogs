class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        """
        secret 1123
                |
        guess  0111
        """
        
        A, B = 0, 0
        countSecret, countGuess = {}, {}
        
        for i in range(len(guess)):
            if secret[i] == guess[i]: A += 1
            countSecret[secret[i]] = countSecret.get(secret[i], 0) + 1
            countGuess[guess[i]] = countGuess.get(guess[i], 0) + 1
        
        B -= A
        for key in countGuess.keys():
            B += min(countSecret.get(key, 0), countGuess.get(key, 0))
            
        return f"{A}A{B}B"

