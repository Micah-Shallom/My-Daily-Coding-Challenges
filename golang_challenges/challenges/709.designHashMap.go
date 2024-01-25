// # Design a HashMap without using any built-in hash table libraries.

// # Implement the MyHashMap class:

// # MyHashMap() initializes the object with an empty map.
// # void put(int key, int value) inserts a (key, value) pair into the HashMap. If the key already exists in the map, update the corresponding value.
// # int get(int key) returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
// # void remove(key) removes the key and its corresponding value if the map contains the mapping for the key.

// # Example 1:

// # Input
// # ["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"]
// # [[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]
// # Output
// # [null, null, null, 1, -1, null, 1, null, -1]

// Explanation
// MyHashMap myHashMap = new MyHashMap();
// myHashMap.put(1, 1); // The map is now [[1,1]]
// myHashMap.put(2, 2); // The map is now [[1,1], [2,2]]
// myHashMap.get(1);    // return 1, The map is now [[1,1], [2,2]]
// myHashMap.get(3);    // return -1 (i.e., not found), The map is now [[1,1], [2,2]]
// myHashMap.put(2, 1); // The map is now [[1,1], [2,1]] (i.e., update the existing value)
// myHashMap.get(2);    // return 1, The map is now [[1,1], [2,1]]
// myHashMap.remove(2); // remove the mapping for 2, The map is now [[1,1]]
// myHashMap.get(2);    // return -1 (i.e., not found), The map is now [[1,1]]

package challenges

import "fmt"


type MyHashMap struct {
	hashMap [][]int
}


func HMConstructor() MyHashMap {
	return MyHashMap{
		hashMap: [][]int{},
	}
}

func (this *MyHashMap) Put (key , value int) {
	for _, lis := range this.hashMap {
		if key == lis[0]{
			lis[1] = value
			return
		}
	}
	this.hashMap = append(this.hashMap, []int{key, value})
}

func (this *MyHashMap) Get (key int) int{
	for _, lis := range this.hashMap{
		if key == lis[0]{
			return lis[1]
		}
	}
	return -1
}

func (this *MyHashMap) Remove(key int) {
	for i, lis := range this.hashMap {
		if key == lis[0] {
			this.hashMap = append(this.hashMap[:i], this.hashMap[i+1:]...)
			return
		}
	}
}



func DesignHashMap() {
	hashmap := HMConstructor()
	hashmap.Put(1, 1)
	hashmap.Put(2, 2)
	hashmap.Put(1,1)
	hashmap.Remove(2)
	hashmap.Put(2,2)
	hashmap.Put(2,1)
	fmt.Println(hashmap.hashMap)
}