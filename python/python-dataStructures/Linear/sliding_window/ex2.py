# Problem: Given an array of positive integers and a target sum, find the minimum length of a contiguous subarray whose sum is greater than or equal to the target sum.

# Example:
# Array: [2, 3, 1, 2, 4, 3]
# Target Sum: 7

def minSubarrayLength(arr: list[int], targetSum: int) -> list[int]:
    start = 0
    minLength = float('inf')
    windowSum = 0
    
    for end in range(len(arr)):
        windowSum += arr[end]

        while windowSum >= targetSum:
            minLength = min(minLength, end - start + 1)
            


print(minSubarrayLength([2, 3, 1, 2, 4, 3], 7))