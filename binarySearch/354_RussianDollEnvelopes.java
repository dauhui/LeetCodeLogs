class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        """
            1:06 - 1:39 use dp with memoize TLE (81/84)
            
            - 2d arrays where [wi, hi] represents width and height of envelope
            - envelope i pack envelop j iff wi > wj & hi > hj
            - return the max number of envolopes can be packed together
            
            1. dp
                - sort according to area
                - put it in or not put it in O(2^n)
                - memoize O(n^2)

                
            2. binary search?
                  v
                a   b
                l   r
                - get the max width
                - if widths are the same, get the max heights
                - if width and height are the same, replace it with same-sized old one
                - proceed
        """
        
        def binarySearch(packSequenceHeights, targetHeight):
            """search for the index of next smaller height"""
            l, r = 0, len(packSequenceHeights)
            while l < r:
                mid = l + (r - l) // 2
                if packSequenceHeights[mid] >= targetHeight:
                    r = mid
                else:
                    l = mid + 1
            return l
        
        # sort according to width
        # if the same, sort according to -height
        envelopes.sort(key=lambda x: [x[0], -x[1]])
        packSequenceHeights = []
        
        for [width, height] in envelopes:
            index = binarySearch(packSequenceHeights, height)
            
            if index > len(packSequenceHeights) - 1:
                packSequenceHeights.append(height)
            else:
                packSequenceHeights[index] = height
            
        return len(packSequenceHeights)
