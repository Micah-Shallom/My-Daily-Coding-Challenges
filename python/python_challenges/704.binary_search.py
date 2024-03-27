# Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

# You must write an algorithm with O(log n) runtime complexity.

 

# Example 1:

# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: 9 exists in nums and its index is 4
# Example 2:

# Input: nums = [-1,0,3,5,9,12], target = 2
# Output: -1
# Explanation: 2 does not exist in nums so return -1
 

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        idx = 0
        for num in nums:
            if num != target:
                idx += 1
            else:
                return idx
        return -1

    def search1(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left+right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid+ 1
            else:
                right = mid - 1
        return -1 

solution = Solution()
nums = [-1,0,3,5,9,12]
target = 9
print(solution.search1(nums,target))