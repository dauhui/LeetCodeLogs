class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        """Calculate the sum of the elements of the rectangle (row2, col2) & (row1, col1)"""
        m, n = len(matrix), len(matrix[0])
        self.matrixSum = [[0]*(n+1)]
        
        for i in range(m):
            self.matrixSum.append([0] + matrix[i])
            for j in range(1, n):
                self.matrixSum[i+1][j+1] += self.matrixSum[i+1][j]

        for i in range(1, m):
            for j in range(n):
                self.matrixSum[i+1][j+1] += self.matrixSum[i][j+1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.matrixSum[row2+1][col2+1]\
                - self.matrixSum[row1][col2+1]\
                - self.matrixSum[row2+1][col1]\
                + self.matrixSum[row1][col1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
