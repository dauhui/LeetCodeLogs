class Solution:
    def searchRange(self, nums, target: int):
        def firstIndex(target):
            l, r = 0, len(nums)
            while l < r:
                mid = l + (r - l)//2
                if nums[mid] >= target:
                    r = mid
                else:
                    l = mid + 1
            return l

        if target not in nums:
            return [-1, -1] # case of target not in array

        return [firstIndex(target), firstIndex(target + 1) - 1]

nums = [5, 7, 7, 8, 8, 10]
target = 8
print(Solution.searchRange(Solution, nums, target))