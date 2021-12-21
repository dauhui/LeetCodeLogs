class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        n1, n2 = list(num1), list(num2)
        
        res, extra = [], 0
        while n1 or n2 or extra:
            num = extra
            
            if n1: num += int(n1.pop())
            if n2: num += int(n2.pop())
                
            if num >= 10: num, extra = num - 10, 1
            else: extra = 0
                
            res.append(str(num))

        return "".join(res[::-1])

