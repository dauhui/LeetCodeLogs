class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        x_zero, y_zero = [], []
        for x in range(m):
            if 0 in matrix[x]:
                x_zero.append(x)
        for y in range(n):
            if 0 in list(zip(*matrix))[y]:
                y_zero.append(y)
        for x in x_zero:
            for y in range(n):
                matrix[x][y] = 0
        for y in y_zero:
            for x in range(m):
                matrix[x][y] = 0

A = [[1,1,1],[1,0,1],[1,1,1]]
Solution.setZeroes(Solution, A)
print(A)