class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        res = 0
        for r in s:
            if r == "L":
                res += 1
                if res == 3: return False
            else:
                res = 0
        return s.count("A") < 2

A = "LALL"
print(Solution.checkRecord(Solution, A))