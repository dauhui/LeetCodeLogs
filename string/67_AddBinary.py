from collections import deque
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a) < len(b): a, b = b, a
        a, b = list(map(int, reversed(a))), list(map(int, reversed(b)))
        
        res, extra = deque([]), 0
        for i in range(len(a)+1):
            
            if i < len(b): 
                res.appendleft(a[i] + b[i] + extra)
            elif i < len(a):
                res.appendleft(a[i] + extra)
            elif extra:
                res.appendleft(extra)
                
            extra = 0
            if res[0] >= 2:
                res[0] -= 2
                extra = 1
                
        return "".join(map(str, res))

