import re
class Solution:
    def solveEquation(self, equation: str) -> str:
        """
        re.findall - find "all" "non-overlaping" matches
        """
        x, a = 0, 0
        side = 1

        # 4 groups: (=) OR (+,-, none) (digits or none) (x or none)
        for eq, sign, num, isx in re.findall('(=)|([+-]?)(\d*)(x?)', equation):
            if eq:
                side = -1
            elif isx:
                x += side * int(sign + '1') * int(num or 1)
            elif num:
                a -= side * int(sign + num)
                
        return 'x={}'.format(a//x) if x else 'No solution' if a else 'Infinite solutions'

