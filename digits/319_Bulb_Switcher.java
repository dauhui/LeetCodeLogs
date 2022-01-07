class Solution {
    public int bulbSwitch(int n) {
        /*
        refer to solution
            - n-bulb
            - for i-round
                - say i=12, (1,12) & (2,6) & (3,4) makes i-bulb turned-off
                - say i=36, (1,36) & (2,18) & (3,12) & (4,9) & (6) makes i-bulb turned-on
        */
        return (int)(Math.sqrt(n));
    }
}
