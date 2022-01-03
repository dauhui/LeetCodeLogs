class Solution {
    public boolean isPowerOfFour(int n) {
        /*
        1. check > 0
        2. check one bit
        3. check odd positions (not power of 4)
           -> since 0101 = 5
           -> 32 bits means eight 5s = 0x(5*8) = 0x55555555 
        */
        return n > 0 && (n & (n-1)) == 0 && (n & 0x55555555) != 0;
    }
}
