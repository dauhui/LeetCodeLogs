class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        table_s, table_t = {}, {}
        if len(s) != len(t): return False
        for chr in s:
            if chr in table_s:
                table_s[chr] += 1
            else:
                table_s[chr] = 1
        for chr in t:
            if chr in table_t:
                table_t[chr] += 1
            else:
                table_t[chr] = 1
        return table_s == table_s

A = "rat"
B = "car"
print(Solution.isAnagram(Solution, A, B))