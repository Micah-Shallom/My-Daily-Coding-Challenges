# Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

# You can use each character in text at most once. Return the maximum number of instances that can be formed.

# Example 1:
# Input: text = "nlaebolko"
# Output: 1

# Example 2:
# Input: text = "loonbalxballpoon"
# Output: 2

# Example 3:
# Input: text = "leetcode"
# Output: 0

class Solution:
    def maxNumberOfBallons(self,txt: str) -> int:
        hashMap = {}
        for i in "ballon":
            if i in hashMap:
                hashMap[i][0] += 1
            hashMap[i] = [0]

        
        for i in txt:
            hashMap[i].append(1)

            
        

solution = Solution()
text = "loonbalxballpoon"
print(solution.maxNumberOfBallons(txt=text))

