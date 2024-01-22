// Given a string array words, return an array of all characters that show up in all strings within the words (including duplicates). You may return the answer in any order.

 

// Example 1:

// Input: words = ["bella","label","roller"]
// Output: ["e","l","l"]
// Example 2:

// Input: words = ["cool","lock","cook"]
// Output: ["c","o"]
 

// Constraints:

// 1 <= words.length <= 100
// 1 <= words[i].length <= 100
// words[i] consists of lowercase English letters.

package challenges

func commonChar(words []string) []string{
	//create a reference hashMap
	refHM := map[rune]int{}

	for _, char := range words[0]{
		refHM[char]++
	}

	//loop through remaining words and create a temp hashmap for each and compare with the reference hashMap
	for i := 1; i <= len(words) - 1; i++ {
		tempHM := map[rune]int{}

		for _, char := range words[i]{
			tempHM[char]++
		}

		//loop through the first and compare with temp, if there is a situation whereby a string in reference isnt in tempHM lets take it down to zero else lets populate the value for that string to the minimum value between tempHM and refHM

		for k, v := range refHM {
			if _, exists := tempHM[k]; !exists{
				refHM[k] = 0
			}else{
				refHM[k] = min(v, tempHM[k])
			}
		}
	}

	//create array to store results
	res := []string{}

	for k, v := range refHM {
		if v != 0 {
			for i := 0; i < v ; i++ {
				res = append(res, string(k))
			}
		}
	}
	return res

}