class Solution:
    def shortestPalindrome(self, s: str) -> str:
        """
        edge cases: "aaaa", ""

        1) babc
        2) duplicate and reverse -> cbab
        1) drop [-1], 2) drop [1]&store
        compare if 1) == 2)
            yes -> return stored value + 1)
            no -> continue droping
        time complexity: O(n)
        space complexity: O(n)
        """
        s_reversed = s[::-1]
        if s_reversed == s: return s
        for i in range(1, len(s)):
            if s[:-i] == s_reversed[i:]:
                return s_reversed[:i] + s

s = "adcda"
print(Solution.shortestPalindrome(Solution, s))
