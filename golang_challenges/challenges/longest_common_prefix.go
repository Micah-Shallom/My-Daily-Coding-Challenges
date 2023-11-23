// Write a function to find the longest common prefix string amongst an array of strings.

// If there is no common prefix, return an empty string "".
// Example 1:

// Input: strs = ["flower","flow","flight"]
// Output: "fl"
// Example 2:

// Input: strs = ["dog","racecar","car"]
// Output: ""
// Explanation: There is no common prefix among the input strings.

// Constraints:

// 1 <= strs.length <= 200
// 0 <= strs[i].length <= 200
// strs[i] consists of only lowercase English letters.

package challenges

import "fmt"

func lcpsolution(strs []string) string {
	if strs == nil{
		return ""
	}
	prefix := " "
	for i:=0; i<len(strs[0]); i++ {
		for _, s := range strs{
			if i == len(s) || s[i] != strs[0][i]{
				return prefix
			}
		}
		prefix += string(strs[0][i])
	}
	return prefix
}


func LCP(){
	strs := []string{"flower","flow","flight"}
	fmt.Println(lcpsolution(strs))
}