class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        """
        - first group: could be shorter than 1+
        - rest groups: k
        """
        
        count, res = 0, []
        for c in reversed(s):
            if not c.isalnum(): continue

            count += 1
            res.append(c.upper())
            if count % k == 0: res.append('-')
        
        if res and res[-1] == '-': res.pop()
        return "".join(res[::-1])

