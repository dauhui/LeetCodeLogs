class Solution:
    def countSubstrings(self, s: str) -> int:
        
        def isPalindrome(i, j):
            if i == j or i + 1 == j: return s[i] == s[j]
            if (i, j) in memo: return memo[(i, j)] 
            memo[(i, j)] = s[i] == s[j] and isPalindrome(i+1, j-1)
            return memo[(i, j)]
        
        count, memo = 0, {}
        for i in range(len(s)):
            for j in range(i, len(s)):
                if isPalindrome(i, j): count += 1
        return count

