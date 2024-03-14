# The next greater element of some element x in an array is the first greater element that is to the right of x in the same array.
# You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.
# For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next greater element of nums2[j] in nums2. If there is no next greater element, then the answer for this query is -1.
# Return an array ans of length nums1.length such that ans[i] is the next greater element as described above.

# Example 1:
# Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
# Output: [-1,3,-1]
# Explanation: The next greater element for each value of nums1 is as follows:
# - 4 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
# - 1 is underlined in nums2 = [1,3,4,2]. The next greater element is 3.
# - 2 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.

# Example 2:
# Input: nums1 = [2,4], nums2 = [1,2,3,4]
# Output: [3,-1]
# Explanation: The next greater element for each value of nums1 is as follows:
# - 2 is underlined in nums2 = [1,2,3,4]. The next greater element is 3.
# - 4 is underlined in nums2 = [1,2,3,4]. There is no next greater element, so the answer is -1.

class Solution:
    def nextGreaterElement(self,list1: list[int], list2: list[int]) -> list[int] :
        arr = []

        for i in range(len(list1)):
            idx = -1

            for j in range(len(list2)):
                if list1[i] == list2[j]:
                    idx = j
               
            if idx != -1:
                found = False

                for k in range(idx,len(list2)):
                    if list2[k] > list2[idx]:
                        arr.append(list2[k])
                        found = True
                        break
                if not found :
                    arr.append(-1)
        return arr  
              
    def nextGreaterElement1(self,list1: list[int], list2: list[int]) -> list[int] :
        nums1idx = {n:i for i, n in enumerate(list1)}
        print(nums1idx)
        res = [-1] * len(list1)

        stack = []
        for i in range(len(list2)):
            curr = list2[i]
            while stack and curr > stack[-1]:
                val = stack.pop()
                idx = nums1idx[val]
                res[idx] = curr
            
            if curr in nums1idx:
                stack.append(curr)
        return res
        
    

         
            


solution = Solution()
list1, list2 = [4,1,2] , [1,4,3,2]
print(solution.nextGreaterElement1(list1,list2))