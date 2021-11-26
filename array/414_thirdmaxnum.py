class Solution(object):
    def thirdMax(self, nums):
        max1 = None
        max2 = None
        max3 = None
        for num in nums:
            if num == max1 or num == max2 or num == max3:
                continue
            if num > max1:
                max3 = max2
                max2 = max1
                max1 = num
            elif num > max2:
                max3 = max2
                max2 = num
            elif num > max3:
                max3 = num
        if max3 == None:
            return max1
        else:
            return max3