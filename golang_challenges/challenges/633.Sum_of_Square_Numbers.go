// Given a non-negative integer c, decide whether there're two integers a and b such that a2 + b2 = c.
// Example 1:

// Input: c = 5
// Output: true
// Explanation: 1 * 1 + 2 * 2 = 5
// Example 2:

// Input: c = 3
// Output: false

package challenges

import "math"

func judgeSquareSum(c int) bool {
	if c < 0 {
		return false;
	};

	sqrtC := int64(math.Sqrt(float64(c)));
	arrSq := []int64{};
	for i := int64(0); i <= sqrtC; i++ {arrSq = append(arrSq, i*i)}
	l, r := 0, len(arrSq) - 1;
	
	for l <= r {
		summed := arrSq[l] + arrSq[r];

		if summed == int64(c){
			return true;
		}else if summed > int64(c){
			r--;
		}else{
			l++;
		}
	}
	return false;
}