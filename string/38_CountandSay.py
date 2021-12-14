class Solution:
    def countAndSay(self, n: int) -> str:
        """
        contiguous section
        1. say the number of character
        2. say the character
        """

        if n == 1: return "1"
        
        s = self.countAndSay(n-1)
        pre, count, res = s[0], 1, []

        for i in range(1, len(s)):
            if pre == s[i]:
                count += 1
            else:
                res.append(str(count) + str(pre))
                pre, count = s[i], 1
                
        res.append(str(count) + str(pre))
        return "".join(res)

