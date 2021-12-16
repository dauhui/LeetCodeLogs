class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_i, t_i = 0, 0
        while s_i < len(s) and t_i < len(t):
            s_i += s[s_i] == t[t_i]
            t_i += 1
        return s_i == len(s)
s = "abc"
t = "cbaabc"
print(Solution.isSubsequence(Solution, s, t))