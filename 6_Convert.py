class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s
        sto = ['']*numRows
        dir = 1
        i = 0
        for chr in s:
            sto[i] += chr
            i += dir
            if i == 0 or i == numRows - 1:
                dir *= -1

        s = ''
        for i in range(numRows):
            s += sto[i]

        return s

s = "AB"
numRows = 1
print(Solution.convert(Solution, s, numRows))
