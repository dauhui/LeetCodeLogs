class Solution(object):
    def findDuplicates(self, nums):
        # Runtime 太高
        sort_nums = sorted(nums)
        set_nums = list(set(nums))
        for i in set_nums:
            sort_nums.remove(i)
        return  sort_nums
        