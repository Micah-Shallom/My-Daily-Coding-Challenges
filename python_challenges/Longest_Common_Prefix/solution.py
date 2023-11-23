class Solution:
    def longestCommonPrefix(self , strs: list[str]) -> str:
        prefix = ""

        if strs is None and len(strs) == 0:
            return prefix

        minimumLength = len(strs[0])
        minimumLength = [len(each) for each in strs if (len(each) < minimumLength)][0]
        
        for x in range(0, minimumLength):
            currentStr = strs[0][x]
            for y in range(0, len(strs)):
                if currentStr != strs[y][x]:
                    return prefix
            prefix += currentStr
        return prefix
    
    def lcp2(self, strs: list[str]) -> str:
        # // a more optimized solution
        if not strs:
            return ""
        prefix  = ""
        for i in range(len(strs[0])):
            for s in strs:
                if i == len(strs) or s[i] != strs[0][i]:
                    return prefix
            prefix += strs[0][i]
        return prefix

if __name__ == '__main__':
    fire = Solution()
    print(fire.longestCommonPrefix(["flower","flow","flight"]))
    print(fire.lcp2(["flower","flow","flight"]))