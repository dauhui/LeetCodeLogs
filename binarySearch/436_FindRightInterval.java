class Solution {
    public int[] findRightInterval(int[][] intervals) {
        /*
            10:58 - 11:35 not solved, turned to solution
        
            - for each interval, use binary search to find the right interval
            - the trick is use start as key to map to the original index
            - we also need a mapping of index to interval
        */
        
        int n = intervals.length;
        int[] starts = new int[n];

        Map<Integer, Integer> indices = new HashMap<>();
        for (int i=0; i<n; i++) {
            indices.put(intervals[i][0], i);
            starts[i] = intervals[i][0];
        }

        Arrays.sort(starts);

        int[] result = new int[n];
        for (int i=0; i<n; i++) {
            int index = Arrays.binarySearch(starts, intervals[i][1]);
            
            if (index >= 0) {
                result[i] = indices.get(starts[index]);
            } else {
                index = -index - 1;
                if (index < n)
                    result[i] = indices.get(starts[index]);
                else
                    result[i] = -1;
            }
            
        }

        return  result;
    }
}