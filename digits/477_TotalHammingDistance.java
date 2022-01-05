class Solution {
    public int totalHammingDistance(int[] nums) {
        /*
        0100
        1110
        0010
          |
          v
        (1*2) -> total hammings at this column = ones * zeros        
        */
        int count = 0, ones = 0;
        for (int i=0; i<32; i++) {
            ones = 0;
            for (int j=0; j<nums.length; j++) {
                if ((nums[j] & 1) == 1) ones += 1;
                nums[j] >>= 1;
            }
            count += ones * (nums.length - ones);
        }
        return count;
    }
}
