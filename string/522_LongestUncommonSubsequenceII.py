class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        """
        - a subsequence of one string but "not the others".
            - n^2 checking
            - start from longer one
        """
        def isSubsequence(w1, w2):
            i = 0
            for c in w2:
                if i < len(w1) and w1[i] == c: i += 1
            return i == len(w1)
        
        strs.sort(key=len, reverse=True)
        for i, w1 in enumerate(strs):
            if all(not isSubsequence(w1, w2) for j, w2 in enumerate(strs) if i != j):
                return len(w1)
        
        return -1

