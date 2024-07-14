# You are given an integer array nums of size n and a positive integer k.

# Divide the array into one or more arrays of size 3 satisfying the following conditions:

# Each element of nums should be in exactly one array.
# The difference between any two elements in one array is less than or equal to k.
# Return a 2D array containing all the arrays. If it is impossible to satisfy the conditions, return an empty array. And if there are multiple answers, return any of them.

# Example 1:

# Input: nums = [1,3,4,8,7,9,3,5,1], k = 2
# Output: [[1,1,3],[3,4,5],[7,8,9]]
# Explanation: We can divide the array into the following arrays: [1,1,3], [3,4,5] and [7,8,9].
# The difference between any two elements in each array is less than or equal to 2.
# Note that the order of elements is not important.
# Example 2:

# Input: nums = [1,3,3,2,7,3], k = 3
# Output: []
# Explanation: It is not possible to divide the array satisfying all the conditions.


class Solution():
    def divideArray(sef, nums: list[int], k: int) -> list[list[int]]:
        nums.sort()

        for i in range(0, len(nums), 3):
            if nums[i+2] - nums[i] > k: return []
        return [nums[i:i+3] for i in range(0, len(nums), 3)]


    def myInitialSolution(sef, nums: list[int], k: int) -> list[list[int]]:
        sorted_nums = sorted(nums)
        arr = list()

        i = 1
        temp_arr = [sorted_nums[0]]
        while i < len(sorted_nums):
            if sorted_nums[i] - temp_arr[-1] <= k:
                temp_arr.append(sorted_nums[i])
            if len(temp_arr)%3 == 0:
                arr.append(temp_arr)
                if i != len(sorted_nums) - 1:
                    temp_arr = [sorted_nums[i+1]]
                    i += 1
            i += 1
        
        if len(sorted_nums) / len(arr) != len(sorted_nums) / 3:
            return []
        return arr




solution = Solution()
nums =  [1,3,4,8,7,9,3,5,1]
k = 2
print(solution.divideArray(nums,k))