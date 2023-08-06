# Find the maximum product of two integers in an array where all elements are positive.

# def maxProd(arr):
#     maxprod = 0
#     for i in range(len(arr)):
#         for j in range(i+1,len(arr)):
#             if maxprod < arr[i]*arr[j]:
#                 maxprod = arr[i]*arr[j]
#     return f"{maxprod}, ({arr[i]}*{arr[j]})"

# def maxProd(arr):
#     arr.sort(reverse=True)
#     print(f"{arr[0]*arr[1]}, ({arr[1]}*{arr[0]})")

def maxProd(arr):
    if len(arr) < 2:
        return "Array should have at least two elements"
    
    max1 = float('-inf')  # Initialize the maximum as negative infinity
    max2 = float('-inf')  # Initialize the second maximum as negative infinity
    
    for num in arr:
        if num > max1:
            max2 = max1
            max1 = num
        elif num > max2:
            max2 = num
    
    maxprod = max1 * max2
    return f"{maxprod}, ({max1}*{max2})"

arr = [1, 7, 3, 4, 9, 5] 
print(maxProd(arr))