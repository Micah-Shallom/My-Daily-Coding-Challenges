package challenges

// ReversePrefix reverses the prefix of a word up to a given index.
func ReversePrefix(word string, ch byte) string {
	n := len(word)
	for i := 0; i < n; i++ {
		if word[i] == ch {
			return reverse(word[:i+1]) + word[i+1:]
		}
	}
	return word
}