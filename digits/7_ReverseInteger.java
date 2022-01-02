class Solution {
    public int reverse(int x) {
        /*
        1. get remainder from 10^0 to 10^d
        2. add remainder to res
        constraint: only 32-bit max/min or return 0
        */
        int res = 0, digit = 0;
        int base = x > 0? String.valueOf(x).length() - 1: String.valueOf(x).length() - 2;
        
        while (x != 0) {
            digit = x % 10;
            if (x > 0 && Integer.MAX_VALUE - res < digit) return 0;
            if (x < 0 && Integer.MIN_VALUE - res > digit) return 0;  
            res += digit * Math.pow(10, base--);
            x /= 10;
        };
        
        return res;
    }
}
