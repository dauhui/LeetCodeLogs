class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if sum(digits) == len(digits)*9:
            digits.insert(0, 0)
        temp = 1
        for i in range(len(digits)-1, -1, -1):
            digits[i] += temp
            temp = 0
            if digits[i] >= 10:
                digits[i] = 0
                temp += 1
            else:
                return digits

digits = [8,9,9]
print(Solution.plusOne(Solution,digits))