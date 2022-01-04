class Solution {
    public String convertToBase7(int num) {
        /*
        1. keep devide 7 until hit 0
        2. add the remainder to res string
        */
        
        if (num == 0) return "0";
        
        boolean isNegative = num < 0;
        String res = "";
        while (num != 0){
            res = Math.abs(num % 7) + res;
            num /= 7;
        };

        return isNegative? "-" + res: res;
    }
}
