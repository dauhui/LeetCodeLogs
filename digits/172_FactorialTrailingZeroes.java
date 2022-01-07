class Solution {
    public int trailingZeroes(int n) {
        /*
        1*2*3*4*5*6*7*8*9*10*...*25 = a*(2*5)^b
                1         1      2
        */
        int count = 0;
        while (n > 0) {
            count += n / 5;
            n = n / 5;
        }
        return count;
    }
}
