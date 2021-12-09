class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        table = {"U":0, "D":0, "R":0, "L":0}
        for dir in moves:
            if dir in table:
                table[dir] += 1
        if table["U"] == table["D"] and table["R"] == table["L"]:
            return True
        return False

A = "UDR"
print(Solution.judgeCircle(Solution, A))