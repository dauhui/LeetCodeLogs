class Solution:
    def guessNumber(self, n: int) -> int:
        lo, hi = 1, n
        while lo < hi:
            mid = lo + (hi - lo)//2
            if guess(mid) == 1:
                lo = mid + 1
            else:
                hi = mid
        return lo