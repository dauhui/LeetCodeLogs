class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t): return False
        for cha in s:
            if cha in t:
                t = t.replace(cha,"",1)
            else:
                return False
        return True

A = "c❦at"
B = "cta❦"
print(Solution.isAnagram(Solution, A, B))