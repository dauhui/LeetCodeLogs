class Solution {
    public boolean validUtf8(int[] data) {
        /*
        for each bytes,
            1. starts with one: ok
            2. starts with n-one + 1-zero: 
                - n bytes (n <= 4)
                - 1 + (n-1) bytes which starts with 10
        */
        int i = 0, n = data.length, mask = 0b10000000, nBytes = 0;
        while (i < n) {
            mask = 0b10000000;
            if ((data[i] & mask) == 0) {
                i += 1;
            } else {
                nBytes = 0;
                while ((mask & data[i]) > 0) {
                    mask >>>= 1;
                    nBytes += 1;
                }
                if (nBytes == 1 || i + nBytes > n || nBytes > 4) return false;
                for (int j=i+1; j<i+nBytes; j++) {
                    if (data[j] >>> 6 != 0b00000010) return false;
                }
                i += nBytes;
            }
        }
        return true;
    }
}
