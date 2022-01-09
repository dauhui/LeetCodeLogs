class Solution {
    public String convertToTitle(int n) {
        /*
            1. convert to higher significant digit
            2. deduct the number by 1
            3. deduct number by 1 for each step; 
                -> n % 26 = 0 <- we use it as Z
                -> n / 26 = a <- should be deducted by 1 since one has been used for Z
        */
        
        String res = "";
        while (n > 0) {
            n--;
            res = (char)(n % 26 + 65) + res;
            n /= 26;
        }        
        return res;
    }
}
