import bisect
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
            10:06 - 10:36 use dp to solve
            
            - find longest strictly increasing subsequence
            1. try all O(2^n)
            2. memoize O(n^2)
            3. leftside, include, rightside -> that's for substring but subsequence!
            4. binary search for next greater O(nlogn)
                - remember to open right side
                - append or update
                            v
                    1 2 ... n
                    l          r
                
        """
        def binarySearch(nums, target):
            """search for the target or next greater"""
            l, r = 0, len(nums)
            while l < r:
                mid = l + (r - l) // 2
                if nums[mid] >= target:
                    r = mid
                else:
                    l = mid + 1
            return l
        
        
        subsequence = []
        for num in nums:
            index = binarySearch(subsequence, num)
            if index > len(subsequence) - 1:
                subsequence.append(num)
            else:
                subsequence[index] = num
        return len(subsequence)