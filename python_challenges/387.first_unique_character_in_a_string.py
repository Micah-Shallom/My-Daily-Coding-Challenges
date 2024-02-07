# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

# Example 1:

# Input: s = "leetcode"
# Output: 0
# Example 2:

# Input: s = "loveleetcode"
# Output: 2
# Example 3:

# Input: s = "aabb"
# Output: -1


class Solution:
    def firstUniqChar(self, s: str) -> int:
        hashmap = {}

        for i in range(len(s)):
            if s[i] in hashmap:
                hashmap[s[i]] += 1
            else:
                hashmap[s[i]] = 1 
        
        for i in hashmap:
            if hashmap[i] == 1:
                return s.index(i)
        return -1


solution = Solution()
s = "leetcode"
print(solution.firstUniqChar(s))