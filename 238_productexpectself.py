class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        output = [1]*len(nums)
        for i in range(len(nums)):
            for j in range(len(nums) - 1):
                temp = nums.pop(i)
                output[i] *= nums[j]
                nums.insert(i, temp)
        return  output