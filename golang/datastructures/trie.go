package datastructures

import "fmt"

type TrieNode struct {
	children map[rune]*TrieNode
	isEnd    bool
}

type Trie struct {
	root *TrieNode
}

func NewTrieNode() *TrieNode {
	return &TrieNode{
		children: make(map[rune]*TrieNode),
		isEnd:    false,
	}
}

func NewTrie() *Trie {
	return &Trie{
		root: NewTrieNode(),
	}
}

func (t *Trie) Insert(word string) {
	node := t.root
	for _, ch := range word {
		if _, exists := node.children[ch]; !exists {
			node.children[ch] = NewTrieNode()
		}
		node = node.children[ch]
	}
	node.isEnd = true
}

func (t *Trie) Search(word string) bool {
	node := t.root
	for _, ch := range word {
		if _, exists := node.children[ch]; !exists {
			return false
		}
		node = node.children[ch]
	}
	return node.isEnd
}

func (t *Trie) StartsWith(prefix string) bool {
	node := t.root

	for _, ch := range prefix {
		if _, exists := node.children[ch]; !exists {
			return false
		}
		node = node.children[ch]
	}
	return true
}

func main() {
	trie := NewTrie()

	trie.Insert("hello")
	trie.Insert("hell")
	trie.Insert("heaven")
	trie.Insert("heavy")

	fmt.Println(trie.Search("hello"))   // true
	fmt.Println(trie.Search("hell"))    // true
	fmt.Println(trie.Search("heaven"))  // true
	fmt.Println(trie.Search("heav"))    // false
	fmt.Println(trie.Search("goodbye")) // false

	// Check for prefixes
	fmt.Println(trie.StartsWith("he"))   // true
	fmt.Println(trie.StartsWith("hea"))  // true
	fmt.Println(trie.StartsWith("hell")) // true
	fmt.Println(trie.StartsWith("goo"))  // false
}
