# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true

# Example 2:
# Input: s = "rat", t = "car"
# Output: false

# Constraints:
# 1 <= s.length, t.length <= 5 * 104
# s and t consist of lowercase English letters.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool :
        s, t = s.lower(), t.lower()

        if len(s) != len(t):
            return False
        
        uniCodeArray = [0 for _ in range(26)]
        
        for i in range(len(s)):
            uniCodeArray[ord(s[i]) - ord("a")] += 1
    
        for i in range(len(t)):
            uniCodeArray[ord(t[i]) - ord("a")] -= 1

        for each in uniCodeArray:
            if each != 0:
                return False
        return True


s = "anagram"
t = "nagaram"
solution = Solution()
print(solution.isAnagram(s,t))