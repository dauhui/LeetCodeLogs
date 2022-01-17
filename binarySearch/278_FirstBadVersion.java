/* The isBadVersion API is defined in the parent class VersionControl.
      boolean isBadVersion(int version); */

public class Solution extends VersionControl {
    public int firstBadVersion(int n) {
        /*
            12:50 - 1:10
            
            - from array [1, n], find the target
            - ggggggbbbbbbbbbb_
              l               r
        */
        int l = 0, r = n + 1;
        while (l < r) {
            int mid = l + (r - l) / 2;
            if (isBadVersion(mid)) r = mid;
            else l = mid + 1;
        }
        return isBadVersion(l)? l: Integer.MAX_VALUE;
    }
}