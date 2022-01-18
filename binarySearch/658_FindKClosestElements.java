class Solution {
    public List<Integer> findClosestElements(int[] arr, int k, int x) {
        /*
            2:03 - 2:33: not solved, turn to solution
            
            - a sorted array with two integer (k, x)
            - return the k closest integers to x in array
            - find the smaller one if distances are the same
                 
                 l         r
                 <---------> <----------->
                 mid         mid+k
                 
                 - x is closer to which one?
        */
       int l = 0, r = arr.length - k;
       while (l < r) {
           int mid = l + (r - l) / 2;
           if (x - arr[mid] > arr[mid+k] - x) l = mid + 1;
           else r = mid;
       } 
       return Arrays.stream(arr, l, l+k).boxed().collect(Collectors.toList());
    }
}