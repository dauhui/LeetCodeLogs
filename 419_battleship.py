class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        cnt = 0
        m = len(board)
        n = len(board[0])
        for x in range(m):
            for y in range(n):
                if board[x][y] == "X" and (board[x - 1][y] == "." or x == 0) and (board[x][y - 1] == "." or y == 0):
                    cnt += 1
        return  cnt
                