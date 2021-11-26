class Solution(object):
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        if ops == []:
            return m*n
        m_add = [ops[i][0] for i in range(len(ops))]
        n_add = [ops[i][1] for i in range(len(ops))]
        return min(m_add)*min(n_add)

ops = [[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3]]
ans = Solution.maxCount(Solution, 3, 3, [])
print(ans)