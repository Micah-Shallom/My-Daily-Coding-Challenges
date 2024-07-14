# Design a HashMap without using any built-in hash table libraries.

# Implement the MyHashMap class:

# MyHashMap() initializes the object with an empty map.
# void put(int key, int value) inserts a (key, value) pair into the HashMap. If the key already exists in the map, update the corresponding value.
# int get(int key) returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
# void remove(key) removes the key and its corresponding value if the map contains the mapping for the key.

# Example 1:

# Input
# ["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"]
# [[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]
# Output
# [null, null, null, 1, -1, null, 1, null, -1]

class Solution:
    def __init__(self):
        self.hashMap = []

    def put(self, key: int, value: int):
        for kv in self.hashMap:
            if key == kv[0]:
                kv[1] = value
                return
        self.hashMap.append([key,value])
        return self.hashMap

    def get(self, key:int):
        for kv in self.hashMap:
            if key == kv[0]:
                return kv[1]
        return -1

    def remove(self, key:int):
        for idx in self.hashMap:
            if key == idx[0]:
                self.hashMap.remove(idx)
        return -1

solution = Solution()
print(solution.put(1,1))
print(solution.put(2,2))
print(solution.get(2))
solution.remove(2)
print(solution.hashMap)
