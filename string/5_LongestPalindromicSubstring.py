class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        top-down: TLE or MLE
        bottom-up: ok but harder
        """
        n = len(s)
        dp = [[False] * n for _ in range(n)]

        res, start, maxLength = "", 0, 0
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if i == j:
                    dp[i][j] = True
                elif s[i] == s[j]:
                    dp[i][j] = i + 1 == j or dp[i + 1][j - 1]
                if dp[i][j] and maxLength < j - i + 1: 
                    maxLength = j - i + 1
                    start = i
        return s[start:start + maxLength]

