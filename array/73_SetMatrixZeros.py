class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """zeros the row(i) and col(j) for all cells (i, j) containing zero"""

        m, n = len(matrix), len(matrix[0])
        zeroInFirstRow, zeroInFirstCol = False, False 
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0: 
                    matrix[i][0] = 0
                    matrix[0][j] = 0
                    if i == 0: zeroInFirstRow = True
                    if j == 0: zeroInFirstCol = True
                        
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        if zeroInFirstRow: matrix[0] = [0]*n  
        if zeroInFirstCol: 
            for i in range(m): 
                matrix[i][0] = 0
                
        return
