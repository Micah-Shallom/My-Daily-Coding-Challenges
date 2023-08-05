# Assignment 1
# ▪ Write a Python code that implements the basic operations of an
# array? (Must include the Update operation)

"""
Basic Operations of an array includes:
- insertion
- deletion
- update 
- search
- length(size)
- access

"""

class Array:
    def __init__(self,maxSize) -> None:
        self.maxSize = maxSize
        self.items = [None] * maxSize
        self.capacity = 0

    # def __str__(self):
    #     return " ".join([str(each)  for each in self.items])

    def display(self):
        print(self.items)
    
    def isFull(self):
        if self.maxSize == self.capacity:
            return True
        else:
            return False

    def isEmpty(self):
        if self.capacity == 0:
            return True
        else: return False
    
    def insert(self,value,location):
        if self.isFull():
            return "The array is filled up"
        else:
            if location > self.maxSize:
                return f"Can only add a value between 0 - {self.maxSize}"
            else:
                self.items[location-1] = value
                self.capacity += 1

    def deletion(self,location):
        if self.isEmpty():
            return "The array is empty"
        else:
            if location > self.maxSize:
                return f"Can only delete a value between 0 - {self.maxSize}"
            else:
                if self.items[location - 1] is None:
                    return "Item already deleted"
                else:
                    self.items[location-1] = None
                    self.capacity -= 1

    def update(self,value, location):
        if self.isEmpty():
            return "The array is empty"
        else:
            if location > self.maxSize:
                return f"Can only update a value between 0 - {self.maxSize}"
            else:
                self.items[location-1] = value

    def length(self):
        return self.capacity


arr = Array(5)
print(arr.insert(1,3))
print(arr.deletion(1))
arr.display()
    



 



# ▪ Implement an enqueue and dequeue operation in Python?




# ▪ Write a Python code that implements the basic operations of a
# linked list?
# class Node:
#     def __init__(self,value) -> None:
#         self.value = value
#         self.next = None


# class CircularSLinkedList:
#     def __init__(self) -> None:
#         self.head = None
#         self.tail = None
    
#     def __iter__(self):
#         node = self.head
#         while node:
#             yield node
#             node = node.next

#     def createCSLL(self,value):
#         new_node = Node(value)
#         new_node.next = new_node
#         self.head = new_node
#         self.tail = new_node


#     def insertNode(self,value):
#         new_node = Node(value)
#         if self.head is None:
#             pass



