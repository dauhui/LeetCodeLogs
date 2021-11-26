class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        ans = []
        while matrix:
            ans += matrix.pop(0)
            matrix[:] = list(zip(*matrix))[::-1]
        return  ans
                
A = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
ans = Solution.spiralOrder(Solution, A)
print(ans)