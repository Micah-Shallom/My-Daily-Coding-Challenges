# 605. Can Place Flowers

# You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

# Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

# Example 1:
# Input: flowerbed = [1,0,0,0,1], n = 1
# Output: true

# Example 2:
# Input: flowerbed = [1,0,0,0,1], n = 2
# Output: false
 

class Solution:
    def can_place_flowers(self, flowerbed: list[int], n: int) -> bool :
        empty = 0 if flowerbed[0] else 1
        
        for f in flowerbed:
           if f:
               n -= int((empty - 1) / 2)
               print(n) 

    def can_place_flowers1(self, flowerbed: list[int], n: int) -> bool :
        for bedIdx in range(1, len(flowerbed)-1):
            if (flowerbed[bedIdx - 1] == 0 and flowerbed[bedIdx + 1] == 0) and flowerbed[bedIdx] != 1:
                flowerbed[bedIdx] = 1
                n -= 1
                print(flowerbed, n)
        return n <= 0

            



solution = Solution()
flowerbed2 = [1,0,0,0,1,0,1]
flowerbed = [1,0,0,0,1] 
n = 2
print(solution.can_place_flowers(flowerbed, n))
