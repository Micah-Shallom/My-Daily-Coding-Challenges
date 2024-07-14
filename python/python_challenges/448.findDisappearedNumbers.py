# Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

# Example 1:
# Input: nums = [4,3,2,7,8,2,3,1]
# Output: [5,6]

# Example 2:
# Input: nums = [1,1]
# Output: [2]


import time

class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        return list(set([each for each in range(1, len(nums)+1)])-set(nums))
    
    def findDisappearedNumbers1(self, nums: list[int]) -> list[int]:
        hashmap = dict()
        for i in range(1,len(nums)+1):
            hashmap[i] = 0
        for i in nums:
            hashmap[i] += 1
        results = [k for k,v in hashmap.items() if v == 0]
        return results
            

with open("./data.csv", 'r') as file:
    data_str = file.read()
    data_list = [int(val) for val in data_str.split(',')]
    

solution = Solution()
nums = [4,3,2,7,8,2,3,1]
start_time = time.time()
print(solution.findDisappearedNumbers1(nums))
end_time = time.time()
print("Elapsed time:", end_time-start_time)