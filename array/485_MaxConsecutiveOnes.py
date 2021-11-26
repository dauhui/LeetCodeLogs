class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        """fin the max length of consecutive-1-subarray"""
        mx, count = 0, 0
        for num in nums:
            if num: 
                count += 1
            else:
                count = 0
            mx = max(mx, count)
        return mx
