class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        """
        i       j  i       j
        a b | c d  e b | x x
        |-> k      |-> k
        
        i           j               
        a b c d e f g x |
        |-------------> k

        
        (1) for every 2k step (i, i+2k]
            -> reverse the substring (i, i+k]
        (2) if the i+2k exceeds len(s)
            -> set the end to the end of string
        """
        
        def reverse(i):
            l, r = i, min(i+k-1, len(s)-1)
            while l < r:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1
            return
                
        s = list(s)
        i = 0
        while i < len(s):
            reverse(i)
            i += 2*k
        
        return "".join(s)

