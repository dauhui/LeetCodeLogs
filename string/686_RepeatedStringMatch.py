class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        """
        Assume b is the substring of repetition of a.
        
            - let's say a consists of two substring s1 & s2 and a = s1 + s2
            - b =      (s1 s2)*k       or
                  s2 + (s1 s2)*k       or 
                       (s1 s2)*k + s1
                       
        Therefore, the max repetition is either k or k+1
        """
        
        k = -(-len(b) // len(a))
        for i in range(2):
            if b in a*(k + i): return k + i
        return -1

