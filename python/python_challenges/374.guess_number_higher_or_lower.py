# We are playing the Guess Game. The game is as follows:

# I pick a number from 1 to n. You have to guess which number I picked.

# Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.

# You call a pre-defined API int guess(int num), which returns three possible results:

# -1: Your guess is higher than the number I picked (i.e. num > pick).
# 1: Your guess is lower than the number I picked (i.e. num < pick).
# 0: your guess is equal to the number I picked (i.e. num == pick).
# Return the number that I picked.

 
# Example 1:
# Input: n = 10, pick = 6
# Output: 6

# Example 2:
# Input: n = 1, pick = 1
# Output: 1

# Example 3:
# Input: n = 2, pick = 1
# Output: 1

class Solution:
    def guess(self, num: int) -> int:
        number = 6
        if num > number:
            return -1
        elif num < number:
            return 1
        else:
            return 0
        

    def guessNumber(self, n: int) -> int:
        low, high = 1, n
        while low <= high:
            mid = (low + high) // 2
            G = self.guess(mid)
            if G == 0:
                print(low,high)
                return mid
            elif G == -1:
                print(low,high)
                high = mid - 1
            else:
                print(low,high)
                low = mid + 1
        return mid


sol = Solution()
print(sol.guessNumber(7))