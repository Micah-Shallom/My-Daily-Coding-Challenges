# 205. Isomorphic Strings

# Given two strings s and t, determine if they are isomorphic.

# Two strings s and t are isomorphic if the characters in s can be replaced to get t.

# All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

# Example 1:

# Input: s = "egg", t = "add"
# Output: true
# Example 2:

# Input: s = "foo", t = "bar"
# Output: false
# Example 3:

# Input: s = "paper", t = "title"
# Output: true

class Solution:
    def isIsomorphic(self, s:str, t:str) -> bool:
        mapST, mapTS = {}, {}

        for i in range(len(s)):
            cS, cT = s[i], t[i]
            if ((cS in mapST and mapST[cS] != cT) or (cT in mapTS and mapTS[cT] != cS)):
                return False
            mapST[cS] = cT
            mapTS[cT] = cS
        return True

    def isIsomorphicMine(self, s: str, t: str) -> bool:
        occurred = dict()

        if s == t:
            return True 
        for idx in range(len(s)):
            if s[idx] in occurred:
                if occurred[s[idx]] == t[idx]:
                    return True
                else:
                    return False
            occurred[s[idx]] = t[idx]
        return False


solution = Solution()
s, t = "egg","add"
print(solution.isIsomorphic(s,t))