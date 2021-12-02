from copy import deepcopy
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        # uni = deepcopy(s)
        # while len(uni) > 1:
        #     uni = uni.replace(uni[-1], "")
        # if len(uni) == 0: return  -1
        # for i in range(len(s)):
        #     if s[i] == uni:
        #         return  i
        l = len(s)
        if l == 1: return 0
        s = list(s)
        for i in range(len(s)):
            uni = s.pop(i)
            if uni not in s: break
            s.insert(i, uni)
            if i == l - 1: return -1
        return i

A = "z"
print(Solution.firstUniqChar(Solution, A))