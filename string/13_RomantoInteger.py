class Solution:
    def romanToInt(self, s: str) -> int:
        """
        - only "one" "smaller" digit can be placed ahead to represent subtraction
        
        M     C    M   X   C   I   V
        1000 100 1000 10  100  1   5
        """
        table = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        
        pre, res = "M", 0
        for c in s:
            res += table[c]
            if table[c] > table[pre]: res += -2*table[pre]
            pre = c
        return res

