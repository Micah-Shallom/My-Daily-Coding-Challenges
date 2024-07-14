# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

 

# Example 1:

# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
# Example 2:

# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.
# Example 3:

# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.

import re

class Solution:
    def isPaindrome(self, s: str) -> bool :
        pattern = r'[^a-zA-Z0-9\s]'

        s = re.sub(pattern,"", s).replace(" ","").lower()

        if s == " ":
            return True
        
        remS = s[::-1]
        
        return s == remS

    def isPalindrome(self, s: str) -> bool:
        s = s.lower()

        r = ""

        for i in range(len(s)):
            if s[i].isalnum():
                r += s[i]

        
        return r == r[::-1]


solution = Solution()
s = "A man, a plan, a canal: Panama"
print(solution.isPalindrome(s))




