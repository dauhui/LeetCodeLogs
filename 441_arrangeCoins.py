class Solution:
    def arrangeCoins(self, n: int) -> int:
        """
        (1 + n)*n//2
        """
        l, r = 1, n
        while r - l > 1:
            mid = l + (r - l)//2
            if (1 + mid)*mid//2 == n:
                return mid
            elif (1 + mid)*mid//2 > n:
                r = mid
            else:
                l = mid
        return l

n = 1
print(Solution.arrangeCoins(Solution, n))