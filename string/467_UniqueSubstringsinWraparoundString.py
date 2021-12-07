class Solution:
    def findSubstringInWraproundString(self, p: str) -> int:
        """
        ...a-za-za-z...

        1. note down how long the consecutive sequence "ends" at each chracter
        2. update according to maximum

        cde"f"
        acde"f"

        {f: 4} => {f: 5}

        """
        res = {c: 1 for c in p}
        length = 1
        
        for i, j in zip(p, p[1:]):
            length = length + 1 if (ord(j) - ord(i)) % 26 == 1 else 1
            res[j] = max(res[j], length)

        return sum(res.values())

