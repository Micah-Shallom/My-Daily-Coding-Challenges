# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
 

# Example 1:

# Input: s = "()"
# Output: true
# Example 2:

# Input: s = "()[]{}"
# Output: true
# Example 3:

# Input: s = "(]"
# Output: false


class Solution:
    pList = ["(",")","[","]","{","}"]

    def isValid1(self, s:str) -> bool:
        stack = []
        # mapping = {')': '(', ']': '[', '}': '{'}
        mapping2 = {"(":")","[":"]","{": "}"}

        for char in s:
            if char in mapping2:  # opening bracket
                stack.append(char)
            else:
                if not stack or mapping2[stack.pop()] != char:
                    return False  # Unmatched closing bracket

    # After iterating through the string, stack should be empty if all brackets are matched
        return len(stack) == 0
                



    def isValid(self, s:str) -> bool:
        closed = False
        hashMap = dict()

        for idx in range(len(s)-1):
            for idy in range(len(self.pList)-1):
                if s[idx] == self.pList[idy]:
                    hashMap[s[idx]] = closed
                    if self.pList[idy+1] in s:
                        hashMap[s[idx]] = True

        return hashMap


solution = Solution()
s = "{[]}"
print(solution.isValid1(s))