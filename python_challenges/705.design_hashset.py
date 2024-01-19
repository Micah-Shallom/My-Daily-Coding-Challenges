# Design a HashSet without using any built-in hash table libraries.

# Implement MyHashSet class:

# void add(key) Inserts the value key into the HashSet.
# bool contains(key) Returns whether the value key exists in the HashSet or not.
# void remove(key) Removes the value key in the HashSet. If key does not exist in the HashSet, do nothing.
 

# Example 1:

# Input
# ["MyHashSet", "add", "add", "contains", "contains", "add", "contains", "remove", "contains"]
# [[], [1], [2], [1], [3], [2], [2], [2], [2]]
# Output
# [null, null, null, true, false, null, true, null, false]

# Explanation
# MyHashSet myHashSet = new MyHashSet();
# myHashSet.add(1);      // set = [1]
# myHashSet.add(2);      // set = [1, 2]
# myHashSet.contains(1); // return True
# myHashSet.contains(3); // return False, (not found)
# myHashSet.add(2);      // set = [1, 2]
# myHashSet.contains(2); // return True
# myHashSet.remove(2);   // set = [1]
# myHashSet.contains(2); // return False, (already removed)

class MyHashSet:

    def __init__(self):
        self.hashSet = []


    def add(self, key: int) -> None:
       if key not in self.hashSet:
           self.hashSet.append(key) 

    def remove(self, key: int) -> None:
        if key in self.hashSet:
            self.hashSet.remove(key)

    def contains(self, key: int) -> bool:
        return key in self.hashSet
            

solution = MyHashSet()
solution.add(1)
solution.add(2)
solution.add(3)
solution.remove(2)
solution.contains(2)
print(solution.contains(3))
