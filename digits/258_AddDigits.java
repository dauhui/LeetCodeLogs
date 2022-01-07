class Solution {
    public int addDigits(int num) {
        /*
        x = a0 + a1*10^1 + a2*10^2 + ... + an*10^n
          = a0 + a1*(9)^1 + a2*(99+1) + ... + an*(9999999..+1)
          = (a0 + a1 + ... + an) + 9b
        */
        if (num == 0) return 0;
        return num % 9 == 0? 9: num % 9;
    }
}
