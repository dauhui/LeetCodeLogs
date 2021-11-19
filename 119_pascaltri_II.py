class Solution(object):
    def generate(self, rowIndex):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        pas = [[1]]
        for i in range(rowIndex):
            
            # still don't know why the line below doesn't work
            # pas.append(pas[i - 1])

            pas.append(list(pas[0]))
            pas[1].append(0)
            for j in range(len(pas[1]) - 1):
                pas[1][j + 1] += pas[0][j]
            pas.pop(0)
        return  pas[0]

A = 5
ans = Solution.generate(Solution,A)
print(ans)