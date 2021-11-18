class Solution(object):
    def firstMissingPositive(self, nums):
        l = len(nums)
        for i in range(l):
            if nums[i] < 0 or nums[i] > l:
                nums[i] = 0
        for i in range(l):
            nums[nums[i]%l] += l
        for i in range(l):
            if nums[i] == 0:
                return  i
        return  l
    
A = [1,3,0,-1]
Solution.firstMissingPositive(Solution, A)