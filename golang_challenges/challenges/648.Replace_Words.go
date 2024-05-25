// In English, we have a concept called root, which can be followed by some other word to form another longer word - let's call this word derivative. For example, when the root "help" is followed by the word "ful", we can form a derivative "helpful".

// Given a dictionary consisting of many roots and a sentence consisting of words separated by spaces, replace all the derivatives in the sentence with the root forming it. If a derivative can be replaced by more than one root, replace it with the root that has the shortest length. If there is a tie between multiple roots of the same length, replace it with the root that occurs first in the dictionary.

// Return the sentence after the replacement. 

 

// Example 1:

// Input: dictionary = ["cat","bat","rat"], sentence = "the cattle was rattled by the battery"
// Output: "the cat was rat by the bat"
// Example 2:

// Input: dictionary = ["a","b","c"], sentence = "aadsfasf absbs bbab cadsfafs"
// Output: "a a b c"

package challenges

import (
	"strings"
)

func replaceWords(dictionary []string, sentence string) string {
	//create a hashmap to store the dictionary
	dict := map[string]bool{}
	for _, word := range dictionary {
		dict[word] = true
	}

	//split the sentence into words
	words := strings.Split(sentence, " ")

	//loop through the words and check if the word is in the dictionary, if it is, replace it with the root word
	for i, word := range words {
		for j := 1; j < len(word); j++ {
			if dict[word[:j]] {
				words[i] = word[:j]
				break
			}
		}
	}

	return strings.Join(words, " ")
}
