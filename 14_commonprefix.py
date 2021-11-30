class Solution(object):
    def longestCommonPrefix(self, strs) -> str:
        strs.insert(0, strs[0])
        for i in range(len(strs[0])):
            for j in range(len(strs) - 1):
                if i >= len(strs[j]) or i >= len(strs[j + 1]) or strs[j][i] != strs[j + 1][i]:
                    return  strs[0][0:i]
        return strs[0]

A = ["flower", "flower", "flower"]
ans = Solution.longestCommonPrefix(Solution, A)
print(ans)