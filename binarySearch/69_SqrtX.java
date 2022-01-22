class Solution {
    /*
        - given a non-gegative integer, return the squae root of x
        - scan from 1 to n O(n)
        - use binary search O(logn)
        - prevent using multiplication
    */
    public int mySqrt(int x) {
        if (x <= 1) return x;
        
        int l = 1, r = x;
        while (l < r) {
            int mid = l + (r - l) / 2;
            if (mid >= x / mid) r = mid;
            else l = mid + 1;
        }
        
        return x / l >= l? l: l-1;
    }
}
