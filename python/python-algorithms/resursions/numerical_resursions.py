# def decToBin(decimal: int, result: str) -> str:
#     if decimal <= 0:
#         return result
#     result = str(decimal % 2) + result 

#     return decToBin(decimal // 2 , result)

# print(decToBin(4, ""))

# def sumNaturalNums(n: int) -> int:
#     if n == 0:
#         return n
#     return n + sumNaturalNums(n-1) 
# print(sumNaturalNums(10))

# def binarySearch(nums: list[int],l , r,  k: int):
#     # l, r = 0, len(nums) - 1
#     # while l <= r :
#     #     mid = (l+r) // 2
#     #     if k == nums[mid]:
#     #         return k
#     #     elif k > nums[mid]:
#     #         l = mid
#     #     else:
#     #         r = mid - 1
#     if l > r:
#         return -1
    
#     mid = (l + r) // 2

#     if k == nums[mid]:
#         return k
    
#     if k < nums[mid]:
#         return binarySearch(nums, l, r=mid-1, k=k)
        
#     return binarySearch(nums, mid, r, k)

# nums = [1,2,3,4,5,6,7,8,9,10]
# print(binarySearch(nums, 0 , len(nums)-1, 9))

class Solution:
    def __init__(self):
        self.powerset = []  # stores all subsets
        self.subset = []  # temporary subset which will be updated as the recursive function executes

    def subsets(self, nums):
        self.backtrack(nums, 0)
        return self.powerset

    def backtrack(self, nums, start):
        self.powerset.append(list(self.subset))  # Add the current subset to the list of solutions

        for i in range(start, len(nums)):
            # Include the current element in the subset
            self.subset.append(nums[i])
            # Recursively explore subsets with the current element included
            self.backtrack(nums, i + 1)
            # Exclude the current element from the subset
            self.subset.pop()  # Backtrack: remove the last element to explore the other choice

sol = Solution()
print(sol.subsets([1,2,3]))