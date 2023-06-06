from random import randint

arr = [randint(1, i) for i in range(1, 500)]

def findBigNum(n):
    if len(n) == 0:
        return 0
    elif n[0] > findBigNum(n[1:]):
        return n[0]
    else:
        return findBigNum(n[1:])

print(findBigNum(arr))


# def findMaxNumRec(sampleArray, n):
#     if n == 1:
#        return sampleArray[0]
#     return max(sampleArray[n-1],findMaxNumRec(sampleArray,n-1))

# print(findMaxNumRec(arr,len(arr)))