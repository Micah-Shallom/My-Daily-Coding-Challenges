// Given two positive integers left and right, find the two integers num1 and num2 such that:

// left <= num1 < num2 <= right .
// Both num1 and num2 are prime numbers.
// num2 - num1 is the minimum amongst all other pairs satisfying the above conditions.
// Return the positive integer array ans = [num1, num2]. If there are multiple pairs satisfying these conditions, return the one with the smallest num1 value. If no such numbers exist, return [-1, -1].

 

// Example 1:

// Input: left = 10, right = 19
// Output: [11,13]
// Explanation: The prime numbers between 10 and 19 are 11, 13, 17, and 19.
// The closest gap between any pair is 2, which can be achieved by [11,13] or [17,19].
// Since 11 is smaller than 17, we return the first pair.
// Example 2:

// Input: left = 4, right = 6
// Output: [-1,-1]
// Explanation: There exists only one prime number in the given range, so the conditions cannot be satisfied.

package challenges

func closestPrimes(left int, right int) []int {
	isPrime := func(n int) bool {
		if n <= 1 {
			return false
		}
		for i := 2; i*i <= n; i++ {
			if n%i == 0 {
				return false
			}
		}
		return true
	}

	primes := []int{}
	ans := []int{-1, -1}

	for i := left; i <= right; i++ {
		if isPrime(i) {
			primes = append(primes, i)
		}
	}

	if len(primes) > 1 {
		mxdiff := int(^uint(0) >> 1)
		for i := 0; i < len(primes)-1; i++ {
			diff := primes[i+1] - primes[i]
			if diff < mxdiff {
				mxdiff = diff
				ans[0] = primes[i]
				ans[1] = primes[i+1]
			}
		}
	}

	return ans
}