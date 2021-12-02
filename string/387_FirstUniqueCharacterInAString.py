class Solution:
    def firstUniqChar(self, s: str) -> int:
        """
        find the first non-repeating character in it and return its index, else -1
        
        - put the item (char as key, index as val) into dictionary
        - if met, del
        - return the min index
        """
        seen = {}
        for i, c in enumerate(s):
            if c not in seen:
                seen[c] = i
            else:
                seen[c] = 1e5

        res = min(seen.values())
        return res if res < 1e5 else -1

