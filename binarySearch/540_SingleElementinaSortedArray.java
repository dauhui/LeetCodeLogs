class Solution {
    public int singleNonDuplicate(int[] nums) {
        /*
            find out the integer which appears exactly once
                1. use xor
                2. binary search 
        */
        int l = 0;
        int r = nums.length - 1;
        while (l < r) {
            int mid = l + (r - l) / 2;
            
            // mid locates at "odd" pos
	    if (mid % 2 == 0){
		if (nums[mid] == nums[mid + 1]) {
		    l = mid + 2;
		} else {
		    r = mid;
	   	}
                
            // mid locates at "even" pos
	    } else {
		if (nums[mid] == nums[mid - 1]) {
		    l = mid + 1;
		} else {
		    r = mid;
		}
	    }
        }
        return nums[l];
    }
}
