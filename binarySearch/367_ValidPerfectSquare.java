class Solution {
    /*
        10:23 - 10:33
    
        - return true is num is perfect square or false
                16 = 4^2
        - scan from (n-1, 2) and check
        - binary search
    */
    public boolean isPerfectSquare(int num) {
        if (num <= 2) return num == 1? true: false;
        
        int l = 2, r = num - 1;
        while (l < r) {
            int mid = l + (r - l) / 2;
            if (num / mid <= mid) r = mid;
            else l = mid + 1;
        }
        return l * l == num? true: false;
    }
}