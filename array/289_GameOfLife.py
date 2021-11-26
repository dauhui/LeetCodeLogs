class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        update the board's next satge based on the rule. 
        
        0: dead
        1: live
        2: live cell and < 2 neighbors -> die
        3: live cell and 2 or 3 neighbors -> continue
        4: live cell and > 3 neighbors -> die
        5: dead cell and ==3 neighbors -> live

        """
        def updateCell(i, j):
            count = 0
            for dx, dy in [[-1,-1], [-1,0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]:
                x = i + dx
                y = j + dy
                if 0 <= x < m and 0 <= y < n and board[x][y] in [1,2,3,4]: count += 1
                    
            if board[i][j] == 1:
                if count < 2: 
                    board[i][j] = 2
                elif count <= 3:
                    board[i][j] = 3
                elif count > 3:
                    board[i][j] = 4
            else:
                if count == 3:
                    board[i][j] = 5
            return

        
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                updateCell(i, j)
        
        for i in range(m):
            for j in range(n):
                if board[i][j] in [1,3,5]:
                    board[i][j] = 1
                else:
                    board[i][j] = 0

        return
