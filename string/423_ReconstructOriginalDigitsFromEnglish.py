class Solution:
    def originalDigits(self, s: str) -> str:
        """
        10 variables and 10 equations
        
        zero - number of "z" == number of zeros
        two - number of "t" == number of twos
        ...
        """
        def number(letter):
            ref = Counter(letter)
            mi = min(count[c] // ref[c] for c in ref)
            for c in ref.keys():
                count[c] -= mi*ref[c]
            return mi
            
        count = Counter(s)
        letters = ["zero", "two", "four", "six", "eight", "one", "three", "five", "seven", "nine"]
        digits = [0, 2, 4, 6, 8, 1, 3, 5, 7, 9]
        
        res = [0]*10
        for i in range(10):
            res[digits[i]] = number(letters[i])
        
        return "".join(str(i)*num for i, num in enumerate(res))

