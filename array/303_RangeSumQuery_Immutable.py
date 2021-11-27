class NumArray:

    def __init__(self, nums: List[int]):
        """Calculate the sum of the elements between indices [left, right]"""
        self.nums = nums
        self.prefix = [0]

        for num in nums:
            self.prefix.append(num + self.prefix[-1])

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix[right+1] - self.prefix[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
