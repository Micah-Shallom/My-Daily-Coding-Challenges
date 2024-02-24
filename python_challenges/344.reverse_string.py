class Solution:
    # def reverseString(self, s: list[str]) -> None:
    #     for i in range(len(s)//2):
    #         op = len(s) -  i - 1
    #         print(op)
    #         temp = s[i]
    #         s[i] = s[op]
    #         s[op] = temp
        
    #     return s
    def reverseString1(self, s: list[str]) -> None:
        l = 0
        r = len(s) -  1
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
        return s

sol = Solution()
print(sol.reverseString1(["h","e","l","l","o"]))