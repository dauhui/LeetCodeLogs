class Solution {
    public int findComplement(int num) {
        long mask = 1;
        int res = 0;
        while (mask <= num) {
            res += (num & mask) > 0? 0: mask;
            mask <<= 1;
        }
        return res;
    }
}
