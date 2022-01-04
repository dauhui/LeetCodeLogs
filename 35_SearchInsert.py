class Solution:
    def searchInsert(self, nums, target: int) -> int:
        left = 0
        right = len(nums)
        if target <= nums[left]:
            return 0

        while (right - left) > 1:
            mid = left + (right - left)//2
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                left = mid
            else:
                right = mid
        return right

        
nums = [1,3,4,5,6]
target = 7
print(Solution.searchInsert(Solution, nums, target))