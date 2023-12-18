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
        triangle = [[1], [1, 1]]`
        if numRows == 1:`
            return triangle[0]
        for i in range(2, numRows):
            prevPascal = triangle[i - 1]
            triangle.append([1])
            for j in range(len(prevPascal) - 1):
                triangle[i].append(prevPascal[j] + prevPascal[j + 1])
            triangle[i].append(1)
        return triangle
    
    def generate1(self, numRows: int) -> list[list[int]]:
        triangle = []
        for i in range(numRows):
            row = [1] * (i + 1)
            for j in range(1, i):
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
            triangle.append(row)
        return triangle

    
    def recursiveGenerate(self, numRows: int) -> list[list[int]]:
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        prevRows = self.recursiveGenerate(numRows-1)
        newRow = [1] * numRows
        print(newRow)
        return prevRows

solution = Solution()
numRows = 5
print(solution.generate1(numRows))