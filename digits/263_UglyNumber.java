import java.util.*;
class Solution {
    public boolean isUgly(int n) {
 	/*
	 1. compare prime factors with {2,3,5}
	     - exclude negative since they contain "-1"
	     - find the prime factors by integer factorization
	 2. keep dividing (refer to sol)
	     - keep divide 2, 3, and 5 until no more full division
	     - remain should only be 1
	*/
	Set<Integer> ref = new HashSet<Integer>(Arrays.asList(2,3,5));
        Set<Integer> res = primeFactorize(n);
        return n > 1? ref.containsAll(res): n == 1;
    }
    
    private Set primeFactorize(int n) {
        Set<Integer> res = new HashSet<Integer>();
        for (int i=2; i<(int)(Math.sqrt(n))+1; i++) {
            if (n % i == 0) {
                res.add(i);
                res.addAll(primeFactorize(n / i));
                return res;
            }
        }
        res.add(n);
        return res;
    }
}
