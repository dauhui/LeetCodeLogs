class Solution:
    def countBinarySubstrings(self, s: str) -> int:

        counts = []
        pre, count = s[0], 1
        for i in range(1, len(s)):
            if s[i] == pre:
                count += 1
            else:
                counts.append(count)
                pre = s[i]
                count = 1        
        counts.append(count)
        
        return sum(min(counts[i], counts[i-1])for i in range(1, len(counts)))

