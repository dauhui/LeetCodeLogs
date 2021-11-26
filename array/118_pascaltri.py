class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        pas = [[1]]
        for i in range(1, numRows):
            
            # still don't know why the line below doesn't work
            # pas.append(pas[i - 1])

            pas.append(list(pas[i - 1]))
            pas[i].append(0)
            for j in range(i):
                pas[i][j + 1] += pas[i - 1][j]
        return  pas

A = 5
ans = Solution.generate(Solution,A)
print(ans)