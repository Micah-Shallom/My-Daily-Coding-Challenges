import array as arr


arr1 = arr.array('i', [1,2,3,4,5,6]) #returns integers
arr2 = arr.array('d', [1,2,3]) #returns floats
print(arr1)
print(arr2)

#array insertion
arr1.insert(0,7)
print(arr1)

#traversing an array
def traverseArray(array):
    for i in array: # ------------ T(0(n))
        print(i) # --------------- T(0(1))

traverseArray(arr1) # hence Time complexity of this operation is T(0(n))
print("-------------------------------------------")
#accessing an element

def accessElement(arr, index):
    if index >= len(arr):
        print('There is no element with such an index value')
    else: print(arr[index])

accessElement(arr1,5)
print("-------------------------------------------")

# searching for an element in an array

def searchInArray(arr,value):
    for i in arr: # ---------------------------------- T(0(n))
        if i == value: # ----------------------------- T(0(1))
            return arr.index(value) # ---------------- T(0(1))
    return "The element does not exist in the array" #-T(0(1))

searchInArray(arr1, 6) # hence Timecomplexity = T(0(n)), Space Complexity = T(0(1))

# Removing a value from a given array
arr1.remove(5)
print(arr1)

print("-------------------------------------------")

# append new element to the end of array
arr1.append(7)
print(arr1)
print("-------------------------------------------")

# extend an array
arr3 = arr.array('i', [10,11,12])
arr1.extend(arr3)
print(arr1)
print("-------------------------------------------")

# add items from list into array using fromlist() method
templist = [20,21,22]
arr1.fromlist(templist)
print(arr1)
print("-------------------------------------------")

# remove last array element using pop() method
arr1.pop()
print(arr1)
print("-------------------------------------------")

# reverse a python array using the reverse() method
arr1.reverse()
print(arr1)
print("-------------------------------------------")

#get array buffer information through buffer_info() method 
print(arr1.buffer_info())
print("-------------------------------------------")

#check for the number of occurences of an element using count() method
print(arr1.count(11))

#converting array to string using tostring() method
# strTemp = arr1.tostring()
# print(strTemp)
print("-------------------------------------------")
print("-------------------------------------------")
print("-------------------------------------------")
print("-------------------------------------------")
print("-------------------------------------------")

#Two dimensional arrays

import numpy as np
twoDims = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
print(twoDims)

# newtwoDims = np.insert(twoDims, 0 , [[0,0,0,0]], axis=1)
# print(newtwoDims)

newtwoDIms = np.append(twoDims, [[0,0,0,0]], axis=0)
print(newtwoDIms)

def accessTwoDims(array, rowIndex, colIndex):
    if rowIndex >= len(array) and colIndex >= len(array[0]):
        print("Incorrect Index")
    else:
        return array[rowIndex][colIndex]
print(accessTwoDims(newtwoDIms,1,2))


def traverse2DArray(array):
    for x in range(len(array)):
        for y in range(len(array[0])):
            print(array[x][y])

traverse2DArray(newtwoDIms)