// # Design a HashSet without using any built-in hash table libraries.

// # Implement MyHashSet class:

// # void add(key) Inserts the value key into the HashSet.
// # bool contains(key) Returns whether the value key exists in the HashSet or not.
// # void remove(key) Removes the value key in the HashSet. If key does not exist in the HashSet, do nothing.

// # Example 1:

// # Input
// # ["MyHashSet", "add", "add", "contains", "contains", "add", "contains", "remove", "contains"]
// # [[], [1], [2], [1], [3], [2], [2], [2], [2]]
// # Output
// # [null, null, null, true, false, null, true, null, false]

// # Explanation
// # MyHashSet myHashSet = new MyHashSet();
// # myHashSet.add(1);      // set = [1]
// # myHashSet.add(2);      // set = [1, 2]
// # myHashSet.contains(1); // return True
// # myHashSet.contains(3); // return False, (not found)
// # myHashSet.add(2);      // set = [1, 2]
// # myHashSet.contains(2); // return True
// # myHashSet.remove(2);   // set = [1]
// # myHashSet.contains(2); // return False, (already removed)

package challenges

import "fmt"


type MyHashSet struct {
	hashSet map[int]bool
}

func HSConstructor() MyHashSet {
	return MyHashSet{
		hashSet: map[int]bool{},
	}
}

func (this *MyHashSet) Add(key int) {
	if _, exists := this.hashSet[key]; !exists{
		this.hashSet[key] = true
	}
}

func (this *MyHashSet) Remove(key int){
	if _, exists := this.hashSet[key]; exists{
		delete(this.hashSet,key)
	}
}

func (this *MyHashSet) contains(key int) bool{
	return this.hashSet[key] 
}

func DesignHashSet(){
	c := HSConstructor()
	c.Add(1)
	c.Add(2)
	c.Add(2)
	c.Remove(2)
	fmt.Println(c)
	fmt.Println(c.contains(1))
}
