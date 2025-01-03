// Given an array of string words, return all strings in words that is a substring of another word. You can return the answer in any order.

// A substring is a contiguous sequence of characters within a string

 

// Example 1:

// Input: words = ["mass","as","hero","superhero"]
// Output: ["as","hero"]
// Explanation: "as" is substring of "mass" and "hero" is substring of "superhero".
// ["hero","as"] is also a valid answer.
// Example 2:

// Input: words = ["leetcode","et","code"]
// Output: ["et","code"]
// Explanation: "et", "code" are substring of "leetcode".
// Example 3:

// Input: words = ["blue","green","bu"]
// Output: []
// Explanation: No string of words is substring of another string.
 


impl Solution {
    pub fn string_matching(words: Vec<String>) -> Vec<String> {
        let mut res:Vec<String> = Vec::new();

        fn find_substring(v: &str, w: &str) -> bool {
            if v.len() > w.len(){
                return false;
            }

            for i in 0..=w.len()-v.len(){
                if &w[i..i+v.len()] == v {
                    return true;
                }
            }
            false
        }

        for v in &words {
            for w in &words{
                if v == w || v.len() > w.len(){
                    continue;
                }

                if find_substring(v, w) {
                    res.push(v.clone());
                    break;
                }
            }
        }
        res
    }
}

