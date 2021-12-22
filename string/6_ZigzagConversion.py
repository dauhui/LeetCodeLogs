class Solution:
    def convert(self, s: str, numRows: int) -> str:
        """
        |   |   |            8*i+0
        |  /|  /|  /         8*i+1, 8*i+7
        | / | / | /  
        |/  |/  |/   ....
        |   |   |            8*i+4
        
        |  |  |   6*i+0
        | /| /|   6*i+1, 6*i+5
        |/ |/ |   6*i+2, 6*i+4
        |  |  |   6*i+3
        
        | | | |   4*i+0
        |/|/|/|   4*i+1, 4*i+3
        | | | |   4*i+2
        
        |||
        |||
        
        |||
        
        - p = period
        """
        if numRows == 1: return s
        p = numRows + numRows - 2
        
        res = []
        for i in range(p//2+1):
            j = p - i
            subString = []
            for k in range(len(s)//p+1):
                if p*k+i < len(s): subString.append(s[p*k+i])
                if i != j % p and p*k+j < len(s): subString.append(s[p*k+j])
            res.append("".join(subString))
            
        return "".join(res)

