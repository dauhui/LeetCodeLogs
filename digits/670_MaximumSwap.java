class Solution {
    public int maximumSwap(int num) {
        int[] last = new int[10];
        char[] arr = Integer.toString(num).toCharArray();
        
        for (int i = 0; i < arr.length; ++i) {
            last[arr[i] - '0'] = i;
        }
        
        for (int i = 0 ; i < arr.length; ++i) {
            for (int j = 9; j > arr[i] - '0'; --j) {
                if (last[j] > i) {
                    char tmp = arr[i];
                    arr[i] = (char) ('0' + j);
                    arr[last[j]] = tmp;
                    return Integer.parseInt(String.valueOf(arr));
                }
            }
        }
        return num;
    }
}
