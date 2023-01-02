class Solution:
    def LongestCommonPrefix(self, strs: list[str]) -> str:
        prefix = ""
        minimumLength = len(strs[0])
        for each in strs:
            if len(each) < minimumLength:
                minimumLength = len(each)

        for x in range(0, minimumLength):
            currentStr = strs[0][x]
            for y in range(len(strs)):
                if currentStr != strs[y][x]:
                    return prefix
            prefix += strs[y][x]
        return prefix

        
fire = Solution()
print(fire.LongestCommonPrefix(["flower","flow","flight"]))