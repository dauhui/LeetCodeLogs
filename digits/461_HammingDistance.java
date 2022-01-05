class Solution {
    public int hammingDistance(int x, int y) {
        int distance = 0;
        for (int i=0; i<32; i++) {
            if (((x ^ y) & 1) == 1) distance += 1;
            x >>= 1;
            y >>= 1;
        }
        return distance;
    }
}
