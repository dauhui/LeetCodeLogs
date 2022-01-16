class Solution {
    public int hIndex(int[] citations) {
        /*
            10:28 - 10:47
        
            - citations[i] for the i-th paper in ascending order
            - compute the researcher's h-index
                - if h papers among n papers have "at least h citations"
                - the other n-h papaers have no more than h
                
                0 1 3 5 6
                    ^
        */
        
        int l = 0, r = citations.length;
        while (l < r) {
            int mid = l + (r - l) / 2;
            if (citations[mid] >= citations.length - mid) {
                r = mid;
            } else {
                l = mid + 1;
            }
        }
        return l <= citations.length? citations.length - l: 0 ;
    }
}