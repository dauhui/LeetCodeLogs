class Solution {
    public int findPeakElement(int[] nums) {
        /*
            2:46 - 3:06
        
            - find 'a' peak
            - use binary search; always go upward
        */
        if (nums.length == 1) return 0;
        
        int l = 0, r = nums.length - 1;
        while (l < r) {
            int mid = l + (r - l) / 2;
            if (nums[mid+1] - nums[mid] > 0) l = mid + 1;
            else r = mid;
        }
        return l;
    }
}