class Solution(object):
    def licenseKeyFormatting(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        s = s[::-1]
        ans = ['']
        cnt = 0
        for i in range(len(s)):
            if s[i] == '-':
                pass
            else:
                cnt += 1
                if cnt%k == 0:
                    ans.append(s[i].upper())
                    ans.append('-')
                else:
                    ans.append(s[i].upper())
        if ans[-1] == '-': ans.pop()
        return ''.join(ans[::-1])

s = "5F3Z-2e-9-w"
k = 4
print(Solution.licenseKeyFormatting(Solution, s, k))