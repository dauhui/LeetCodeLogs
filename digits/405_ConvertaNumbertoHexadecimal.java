class Solution {
    /*
         1 = 0000000000000001
        -1 = 1111111111111111 = 0xffffffff
    */
    
    char map[] = {'0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f'};
    
    public String toHex(int num) {
        if (num == 0) return "0";
        
        String res = "";
        while (num != 0) {
            res = this.map[(num & 15)] + res;
            num = (num >>> 4);
        }
        
        return res;
    }
}
