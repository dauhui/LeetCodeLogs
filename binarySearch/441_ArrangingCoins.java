class Solution {
    /*
        1:11 - 1:21
    
        - a staircase consists of k rows where i-th row has i coins
        - except for last row which may be incomplete
        - return the number of complete rows
        
            8 = 1+2+3+2
            
        - add from 1 until the number of coins exceeds n
        - coins from 1 to n rows will have
            - (1+n)*n/2
            - binary search
            - use double to compare
    */
    public int arrangeCoins(int n) {
        int lo = 1, hi = n;
        while (lo < hi) {
            int mid = lo + (hi - lo) / 2;
            if ((1+mid)/2 >= n/mid) hi = mid;
            else lo = mid + 1;
        }
        System.out.println(lo);
        return (1+lo)/2. > n/(double)(lo)? lo-1: lo;
    }
}