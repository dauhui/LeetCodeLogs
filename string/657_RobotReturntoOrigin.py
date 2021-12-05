class Solution:
    def judgeCircle(self, moves: str) -> bool:
        if len(moves) % 2 != 0: return False
        
        dx, dy = 0, 0
        for move in moves:
            if move == "U":
                dy += 1
            elif move == "D":
                dy -= 1
            elif move == "R":
                dx += 1
            else:
                dx -= 1
        return (dx, dy) == (0, 0)

