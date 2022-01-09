class Solution {
    public int titleToNumber(String columnTitle) {
        /*int 'A' == 65*/
        int res = 0;
        for (int i=0; i<columnTitle.length(); i++) {
            res *= 26;
            res += (int) columnTitle.charAt(i) - 64;
        }
        return res;
    }
}
