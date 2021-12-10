class Solution:
    def optimalDivision(self, nums: List[int]) -> str:
        """
        1. dfs top-down dp: TLE (83/93)
            - can always open
            - if has open, can open, close or not
            
        2. math
            - element is either in the numerator or denominator of the final fraction
            - A0 / (A1 / A2 .... / An) = A0 * A2 * ... * An / A1
        """
        
        s = list(map(str, nums))
        if len(nums) <= 2: return "/".join(s)
        return "{}/({})".format(s[0], "/".join(s[1:]))

