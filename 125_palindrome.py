class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = [item for item in s.lower() if item.isalnum()]
        for i in range(int(round(len(s)/2))):
            if s[i] != s[-i - 1]:
                return  False
        return  True

A = "a"
ans = Solution.isPalindrome(Solution, A)
print(ans)