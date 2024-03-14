# Given a string s, sort it in decreasing order based on the frequency of the characters. The frequency of a character is the number of times it appears in the string.

# Return the sorted string. If there are multiple answers, return any of them.
# Example 1:

# Input: s = "tree"
# Output: "eert"
# Explanation: 'e' appears twice while 'r' and 't' both appear once.
# So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
# Example 2:

# Input: s = "cccaaa"
# Output: "aaaccc"
# Explanation: Both 'c' and 'a' appear three times, so both "cccaaa" and "aaaccc" are valid answers.
# Note that "cacaca" is incorrect, as the same characters must be together.
# Example 3:

# Input: s = "Aabb"
# Output: "bbAa"
# Explanation: "bbaA" is also a valid answer, but "Aabb" is incorrect.
# Note that 'A' and 'a' are treated as two different characters.

class Solution:
    def frequencySort(self, s: str) -> str:
        from collections import defaultdict
        hashmap = defaultdict(int)
        res = ""

        for c in s:
            hashmap[c]+=1

        hashmap = dict(sorted(hashmap.items(), key=lambda item: item[1], reverse=True))
        
        for each in hashmap:
            res += each * hashmap[each]
        return res
    
    def frequencySort1(self, s: str) -> str:
        from collections import defaultdict

        count =  defaultdict(int)
        bucket = defaultdict(list)

        for c in s:
            count[c] += 1
        
        for char, cnt in count.items():
            bucket[cnt].append(char)

        res = []
        for i in range(len(s), 0, -1):
            for c in bucket[i]:
                res.append(c * i)

        return "".join(res)

solution = Solution()
s = "Aabb"
print(solution.frequencySort1(s))