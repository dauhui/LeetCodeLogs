class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        extra = 1
        for i in reversed(range(len(digits))):
            digits[i] += extra
            extra = 0
            if digits[i] >= 10:
                extra = 1
                digits[i] -= 10
            if extra == 0: return digits
        return [extra] + digits

