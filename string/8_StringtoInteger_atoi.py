class Solution:
    def myAtoi(self, s: str) -> int:
        """
        1. ignore leading whitespace
        2. if next character == "+" positive; "-" negative
        3. read until non-digit or the end
        4. convert digits to integer ex. "0032" -> "32"; "" -> "0"
        5. [-2^31, 2^31-1]
        """
        if not s: return 0
        
        INT_MIN, INT_MAX = -2**31, 2**31-1
        
        i, res, sign = 0, [], 1
        while i < len(s) and s[i] == " ": i += 1
            
        if i < len(s) and (s[i] == "+" or s[i] == "-"): 
            if s[i] == "-": sign = -1
            i += 1
            
        while i < len(s):
            if s[i].isnumeric():
                res.append(int(s[i]))
                i += 1
            else:
                break

        digits, res = res or [0], 0     
        for i, digit in enumerate(reversed(digits)):
            res += sign*digit*10**i
            if res >= INT_MAX: return INT_MAX
            if res <= INT_MIN: return INT_MIN
            
        return res

