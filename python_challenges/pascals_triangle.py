# Given an integer numRows, return the first numRows of Pascal's triangle.

# Example 1:

# Input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
# Example 2:

# Input: numRows = 1
# Output: [[1]]
 

# Constraints:

# 1 <= numRows <= 30
class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        triangle = [[1], [1, 1]]
        if numRows == 1:
            return triangle[0]
        for i in range(2, numRows):
            prevPascal = triangle[i - 1]
            triangle.append([1])
            for j in range(len(prevPascal) - 1):
                triangle[i].append(prevPascal[j] + prevPascal[j + 1])
            triangle[i].append(1)
        return triangle

solution = Solution()
numRows = 5
print(solution.generate(numRows))

solution = Solution()
numRows = 5
print(solution.generate(numRows))