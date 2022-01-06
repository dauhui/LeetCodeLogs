class Solution {
    public boolean hasAlternatingBits(int n) {
        int pre = n & 1, cur = 0;
        while (n > 0) {
            n >>>= 1;
            cur = n & 1;
            if (pre + cur != 1) return false;
            pre = cur;
        }
        return true;
    }
}
