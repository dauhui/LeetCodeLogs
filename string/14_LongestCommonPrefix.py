class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        find the longest common prefix string amongst an array of strings
        
        - find the min length of all since there won't be any longer common string
        - scan through each string's index and compare
        """
        n = len(strs)
        if n == 1: return strs[0]
        
        minLength = min(map(len, strs))
        for i in range(minLength):
            for j in range(n-1):
                if strs[j][i] != strs[j+1][i]: return strs[0][:i]

        return strs[0][:minLength]
