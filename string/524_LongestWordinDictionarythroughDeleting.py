class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        
        def isSubsequence(s, t):
            s = list(s)
            for c in reversed(t):
                if s and c == s[-1]: s.pop()
                if not s: return True
            return s == []
        
        res = None
        for string in dictionary:
            if not res:
                if isSubsequence(string, s):
                    res = string
            elif len(res) <= len(string):
                if len(res) == len(string) and res > string and isSubsequence(string, s):
                    res = string
                if len(res) < len(string) and isSubsequence(string, s):
                    res = string
        return res if res else ""

