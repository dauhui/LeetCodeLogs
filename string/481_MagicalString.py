class Solution:
    def magicalString(self, N: int) -> int:
        """
        1 2 2 1 1
                n
            m
            
        1. 1 and 2 are alternating
        2. the repetition is depending on m
        """

        m, magicNumber, base = 2, "122", "1"
        count = 1
        while len(magicNumber) < N:
            for i in range(int(magicNumber[m])):
                magicNumber += base
                if base == "1": count += 1
                if len(magicNumber) == N: return count
            base = "2" if base == "1" else "1"
            m += 1
        return count

