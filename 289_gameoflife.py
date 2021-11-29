from copy import deepcopy

class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        copy_board = deepcopy(board)
        cnt = 0
        # neighbors
        for x in range(m):
            for y in range(n):
                nei = [copy_board[_x][_y]
                for _x, _y in [(x-1,y-1),(x-1,y),(x-1,y+1),(x,y-1),(x,y+1),(x+1,y-1),(x+1,y),(x+1,y+1)]
                if 0 <= _x < m and 0 <= _y < n]

                for i in range(len(nei)):
                    if nei[i] == 1:
                        cnt += 1
                
                if copy_board[x][y] == 1:
                    if cnt == 2 or cnt == 3:
                        board[x][y] = 1
                    else:
                        board[x][y] = 0
                else:
                    if cnt == 3:
                        board[x][y] = 1
                    else:
                        board[x][y] = 0
                
                cnt = 0

A = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
Solution.gameOfLife(Solution, A)
print(A)
