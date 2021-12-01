class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str

        s = "a b c d e f g h"
        k = 3

        1st:
              i+
              0 1 2 3 4 5
        pick "a b c d e f"

        for 0 1 2: reverse: [::-1]
        """
        s = list(s)
        for i in range(0, len(s), 2*k):
            s[i:i+k] = [item for item in s[i:i+k]][::-1]
        
        return  "".join(s)

A = "abcdefgh"
print(Solution.reverseStr(Solution, A, 3))