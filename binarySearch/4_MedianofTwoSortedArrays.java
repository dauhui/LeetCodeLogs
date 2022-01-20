class Solution {
    /*
        10:34 - 11:04
    
        - find the median of two sorted array
        - arange numbers one-by-one based on two pointer and get the middle one O(n+m)
        
                [1, 2] [3, 4] -> [1]
                 ^      ^
                 
                [1, 2] [3, 4] -> [1,2]
                    ^   ^
                    
        - binary search?
            - find a partition of which 
                - even: size of left side equals size of right side
                - odd: size of left sise equals size of right side + 1
            - we can do the binary search on each partition of shorter array
            - since total length is fixed, we know the partition of the other array  
            
                [1 | 2,5] 
                  
                [3,4,7 | 10]
                
            - median
                min(left side) <= min(right side)
    */
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int n = nums1.length, m = nums2.length;
        int i = 0, j = 0;
        int[] nums = new int[n + m];
        while (i < n || j < m) {
            if (i == n) nums[i+j] = nums2[j++];
            else if (j == m) nums[i+j] = nums1[i++];
            else if (nums1[i] > nums2[j]) nums[i+j] = nums2[j++];
            else nums[i+j] = nums1[i++];
        }
        return (n + m) % 2 != 0? nums[(n + m) / 2]: (nums[(n + m) / 2] + nums[(n + m) / 2 - 1]) / 2.;
    }
}