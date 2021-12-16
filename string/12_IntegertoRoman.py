class Solution:
    def intToRoman(self, num: int) -> str:    

        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        symbols = ['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
        
        res, i = [], 0
        while num:
            q, num = num // values[i], num % values[i]
            res.append(symbols[i]*q)
            i += 1
        return "".join(res)

