class Solution:
    def __init__(self):
        self.values = [
            1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 
            16, 17, 18, 19, 20, 30, 40, 50, 60, 70, 80, 90, 100, 
            1000, 1000000, 1000000000
        ]
        self.symbols = [
            'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine',
            'Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen',
            'Seventeen', 'Eighteen', 'Nineteen', 'Twenty', 'Thirty', 'Forty', 'Fifty',
            'Sixty', 'Seventy', 'Eighty', 'Ninety', 'Hundred', 'Thousand', 'Million',
            'Billion'
        ]
        
    def convert(self, num):
        if not num: return "Zero"
        if num in self.values: return self.symbols[self.values.index(num)]
        
        res, i = [], len(self.values) - 1
        while num:
            q, num = num // self.values[i], num % self.values[i]
            if q >= 1:
                if self.values[i] >= 100: res.append(self.convert(q))
                res.append(self.symbols[i])
            i -= 1
        
        return " ".join(res)        
                
    def numberToWords(self, num: int) -> str:
        res = self.convert(num)
        firstLetter = res.split()[0]
        if firstLetter in self.symbols and self.symbols.index(firstLetter) >= len(self.symbols) - 4:
            return "One " + res
        else:
            return res

