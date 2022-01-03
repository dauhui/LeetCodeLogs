class Solution {
    public boolean isPowerOfThree(int n) {
        /*
            1. power of three: 3*3*...
                -> keep divide 3 until meet 1
            2. find the max power of 3 within bound
                -> such number will be diveded by all other power of three
        */
        return n > 0 && (1162261467 % n) == 0;
    }
}
