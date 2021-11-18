class Solution(object):
    def hIndex(self, citations):
        ans = 0
        for h in range(max(citations) + 1):
            cnt = len([item for item in citations if item >= h])
            if h <= cnt:
                ans = max(ans, h)
        return  ans

A = [100]
ans = Solution.hIndex(Solution,A)
print(ans)