class Solution {
    public int searchInsert(int[] nums, int target) {
        
            1020 - 1030
            
            - return index if found the target
            - else return index where it were inserted in order
            - next big
            
                    1 3 5 6 
                    ^     ^
                    
                    v
                    a b
                    l r
        
        
        int l = 0, r = nums.length;
        while (l  r) {
            int mid = l + (r - l)  2;
            if (nums[mid] = target) {
                r = mid;
            } else {
                l = mid + 1;
            }
        }
        return l;
    }
}