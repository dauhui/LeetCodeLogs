class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        """
        abcd
        cddab > cdd abcd dab

        aabb
        bbaab > bb aabb baab
        """
        if b in a*(len(b)//len(a) + 2):
            if b in a*(len(b)//len(a) + 1):
                if b in a*(len(b)//len(a)):
                    return len(b)//len(a)
                return len(b)//len(a) + 1
            return len(b)//len(a) + 2
        return -1

a = 'abc'
b = 'cabcabca'
print(Solution.repeatedStringMatch(Solution, a, b))