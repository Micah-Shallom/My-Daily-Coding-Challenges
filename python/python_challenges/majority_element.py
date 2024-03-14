# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

# Example 1:

# Input: nums = [3,2,3]
# Output: 3
# Example 2:

# Input: nums = [2,2,1,1,1,2,2]
# Output: 2

import math

class Solution:
    def majorityElement(self, arr: list[int]) -> int:
        bench = math.floor(len(arr)/2)
        hashmap = {}
        for val in arr:
            if val in hashmap:
                hashmap[val] += 1
            else:
                hashmap[val] = 0
        
        for each in hashmap:
            if hashmap[each] >= bench:
                return each
    def majorityElement1(self, arr: list[int]) -> int:
        # arr.sort()
        # return arr[len(arr)//2]
    
        # using the booyer moore voting algorithm
        res, count = 0, 0

        for n in arr:
            if count == 0:
                res = n
            count += (1 if n == res else -1)
            
        return res

solution = Solution()
arr = [2,2,2,2,5,6,7,8,9]
print(solution.majorityElement1(arr))
 