// # Given an array nums of distinct positive integers, return the number of tuples (a, b, c, d) such that a * b = c * d where a, b, c, and d are elements of nums, and a != b != c != d.

 

// # Example 1:

// # Input: nums = [2,3,4,6]
// # Output: 8
// # Explanation: There are 8 valid tuples:
// # (2,6,3,4) , (2,6,4,3) , (6,2,3,4) , (6,2,4,3)
// # (3,4,2,6) , (4,3,2,6) , (3,4,6,2) , (4,3,6,2)
// # Example 2:

// # Input: nums = [1,2,4,5,10]
// # Output: 16
// # Explanation: There are 16 valid tuples:
// # (1,10,2,5) , (1,10,5,2) , (10,1,2,5) , (10,1,5,2)
// # (2,5,1,10) , (2,5,10,1) , (5,2,1,10) , (5,2,10,1)
// # (2,10,4,5) , (2,10,5,4) , (10,2,4,5) , (10,2,5,4)
// # (4,5,2,10) , (4,5,10,2) , (5,4,2,10) , (5,4,10,2)

use std::collections::HashMap;

impl Solution {
    pub fn tuple_same_product(nums: Vec<i32>) -> i32 {
        let mut hm = HashMap::new();
        let n = nums.len();
        let mut ans = 0;

        for i in 0..n {
            for j in i+1..n {
                let prod = nums[i] * nums[j];
                *hm.entry(prod).or_insert(0) += 1;
            }
        }

        for &count in hm.values() {
            if count >= 2 {
                ans += count*(count-1)*4;
            }
        }
        ans
    }
}
