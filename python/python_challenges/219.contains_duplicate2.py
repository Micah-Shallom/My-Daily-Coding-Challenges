# Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.
# Example 1:

# Input: nums = [1,2,3,1], k = 3
# Output: true
# Example 2:

# Input: nums = [1,0,1,1], k = 1
# Output: true
# Example 3:

# Input: nums = [1,2,3,1,2,3], k = 2
# Output: false


class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k:int) -> bool:
        num_indices = {}

        for idx, num in enumerate(nums):
            if num in num_indices and idx - num_indices[num] <= k :
                return True
            num_indices[num] = idx
        return False

    def initialSolution(self, nums: list[int], k:int) -> bool:
        l, r = -1, -1
        hM = {}
        for each in nums:
            if each in hM:
                hM[each] += 1
            else:
                hM[each] = 1
        
        repeatednums = []
        for val,count in hM.items():
            if count > 1:
                repeatednums.append(val)
        
        for i in repeatednums:
            for j in range(len(nums)):
                if l != -1 and nums[j] == i:
                    r = j
                if nums[j] == i and r == -1:
                    l = j
            
            
            if abs(l - r) <= k:
                return True
        return False

                


solution = Solution()
nums,k = [1,2,3,1], 3
print(solution.containsNearbyDuplicate(nums,k))