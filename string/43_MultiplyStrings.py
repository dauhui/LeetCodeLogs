class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        """
        (a+b) (c+d) = a(c+d) + b(c+d) = ac + ad + bc + bd
        
        - O(n^2)
        """
        A = [int(num)*10**(len(num1) - 1 - i) for i, num in enumerate(num1)]
        B = [int(num)*10**(len(num2) - 1 - i) for i, num in enumerate(num2)]
        
        res = 0
        
        for a in A:
            for b in B:
                res += a*b
        
        return str(res)

