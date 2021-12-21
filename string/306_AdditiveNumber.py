class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        """
        - at least three numbers
        - except first two, a[i+2] = a[i+1] + a[i]
        
        - dfs
            - prevent leading zero
        """
        def dfs(i, a1, a2):
            if i >= len(num): return i == len(num)    
            if len(a1) > 1 and a1[0] == "0": return False
            if len(a2) > 1 and a2[0] == "0": return False
            
            a3 = str(int(a1) + int(a2))
            if num[i: i+len(a3)] == a3 and dfs(i+len(a3), a2, a3): return True
            
            return False
        
        # traverse all pairs of (a[1], a[2])
        for i in range(len(num) - 2):
            for j in range(i+1, len(num) - 1):
                if dfs(j+1, num[:i+1], num[i+1:j+1]): return True
        return False

