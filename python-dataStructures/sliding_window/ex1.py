################### FIXED SIZED SLIDING WINDOW ########################

# Problem: Given an array of integers and a window size, find the maximum sum of any subarray of the given window size.

# Example:
# Array: [4, 2, 7, 1, 3, 6]
# Window Size: 3

def maxWindowSize(arr: list[int], size: int) -> list[int] :
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