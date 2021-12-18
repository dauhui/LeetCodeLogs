class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s = list(s)
        for c in reversed(t):
            if s and c == s[-1]: s.pop()
            if not s: return True
        return s == []

