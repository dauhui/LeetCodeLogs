class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        matrix[:] = list(zip(*matrix[::-1]))

A = [[1,2,3],[4,5,6],[7,8,9]]
ans = Solution.rotate(Solution, A)
print (A)