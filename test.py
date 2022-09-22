class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str :
        prefix = ""

        if strs is None or len(strs) == 0:
            return prefix

        minLen = len(strs[0])
        for each in strs:
            minLen = min(minLen, len(each))
        
        for x in range(0, minLen):
            currentStr = strs[0][x]
            
            for y in range(0, len(strs)):
                if strs[y][x] != currentStr:
                    return prefix
            prefix += currentStr
        return prefix
        

if __name__ == '__main__':
    me = Solution()
    print(me.longestCommonPrefix(["flower","flow","flight"]))
    # print(me.longestCommonPrefix(["dog","racecar","car"]))