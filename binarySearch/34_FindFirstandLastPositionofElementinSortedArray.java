class Solution {
    public int[] searchRange(int[] nums, int target) {
        /*
            1. nums are sorted in non-decreasing order
            2. find the starting and ending pos of given target
            3. or return [-1, -1] if not found
            
            5 7 7 8 8 10
                  ^ ^
            v
            a b
            l r
        */
        if (nums.length == 0) return new int[] {-1, -1};
        
        int l = 0;
        int r = nums.length;
        while (l < r) {
            int mid = l + (r - l) / 2;
            if (nums[mid] >= target) r = mid;
            else l = mid + 1;
        }
        
        if (l >= nums.length || nums[l] != target) return new int[] {-1, -1};
        while (r < nums.length && nums[r] == target) r += 1;
        return new int[] {l, r-1};
    }
}
