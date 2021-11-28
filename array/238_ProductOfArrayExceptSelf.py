class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        return an array s.t. answer[i] equals to the product of all the resr elements

        - prefix prodcut and suffix product
        - shift it by 1 and -1
        - use res as storage to realize O(1) in space-complexity

        1 | 1  2  3  4 | 1
        ->  1  1  2  6  
           24 12  4  1 <- 
        """
        
        res = []
        
        product = 1
        for i in range(len(nums)):
            res.append(product)
            product *= nums[i]
            
        product = 1
        for j in range(len(nums)-1, 0, -1):
            product *= nums[j]
            res[j-1] *= product
            
        return res
