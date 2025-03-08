// You are given a string s.

// Your task is to remove all digits by doing this operation repeatedly:

// Delete the first digit and the closest non-digit character to its left.
// Return the resulting string after removing all digits.

// Example 1:

// Input: s = "abc"

// Output: "abc"

// Explanation:

// There is no digit in the string.

// Example 2:

// Input: s = "cb34"

// Output: ""

// Explanation:

// First, we apply the operation on s[2], and s becomes "c4".

// Then we apply the operation on s[1], and s becomes "".

 
impl Solution {
    pub fn clear_digits(s: String) -> String {
        let mut sk: Vec<char> = Vec::new();

        for c in s.chars() {
            if c.is_numeric(){
                if !sk.is_empty(){
                    sk.pop();
                }
            }else{
                sk.push(c)
            }
        }

        sk.iter().collect()
    }
}
