################### FIXED SIZED SLIDING WINDOW ########################

# Problem: Given an array of integers and a window size, find the maximum sum of any subarray of the given window size.

# Example:
# Array: [4, 2, 7, 1, 3, 6]
# Window Size: 3

def maxWindowSize(arr: list[int], size: int) -> list[int]:
    windowSum = sum(arr[:size])
    maxSum = windowSum

    for end in range(size, len(arr)):
        windowSum += arr[end] - arr[end-size]
        maxSum = max(windowSum, maxSum)
    return maxSum

print(maxWindowSize([4, 2, 1, 7, 8, 1, 2, 8, 1, 0], 3))



# Problem: Given an array of integers and a window size, find the average of all subarrays of the given window size.

# Example:
# Array: [1, 3, 2, 6, -1, 4, 1, 8, 2]
# Window Size: 3

def findAverages(arr: list[int], size: int) -> list[int]:
    start = 0
    windowSum = sum(arr[:size])
    averages = []

    for end in range(size, len(arr)):
        average = round(windowSum / size, 2)
        averages.append(average)
        windowSum += arr[end] - arr[start]
        start += 1

    return averages

print(findAverages([1, 3, 2, 6, -1, 4, 1, 8, 2], 3))

# Given an integer array nums and an integer k, find the maximum product of any subarray of length k.

# Example:
# Input: nums = [2, 3, -2, 4, 1, -5, 6], k = 3
# Output: 48
# Explanation: The subarray with maximum product is [4, 1, -5], which has a product of 48.


def maxProductSubArray(arr: list[int], size: int) -> list[int]:
    start = 0
    windowSize = arr[:size]
    windowProduct = [for e]

print(maxProductSubArray([2, 3, -2, 4, 1, -5, 6], 3))



# Problem: Longest Substring Without Repeating Characters

# Description:
# Given a string s, find the length of the longest substring without repeating characters.

# Example:
# Input: "abcabcbb"
# Output: 3
# Explanation: The longest substring without repeating characters is "abc", which has a length of 3.

def subStrings(strs: str):
    start = 0
    end = 0
    charSet = set()
    maxLength = 0

    while end < len(strs):
        if strs[end] in charSet:
            charSet.remove(strs[start])
            start += 1
        else:
            charSet.add(strs[end])
            maxLength = max(maxLength, end - start + 1)
            end += 1
    return charSet, maxLength


        

print(subStrings("abcabcbb"))
