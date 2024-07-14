# find the missing number in an array of numbers

arr1 = [1,2,3,4,5,7,8,9,10]

def findmissing(lst,n):
    sumOfLst = n*(n+1)/2
    return sumOfLst - sum(lst)

print(findmissing(arr1, max(arr1)))