class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str :
        lcp = ""

        if strs is None or len(strs) == 0:
            return lcp

        minLength = len(strs[0])
        for each in strs:
            minLength = min(minLength , len(each))

        for x in range(0, minLength):
            currentStr = strs[0][x]

            for y in range(0, len(strs)):
                if strs[y][x] != currentStr:
                    return lcp
            lcp += currentStr
        return lcp


if __name__ == "__main__":
    me = Solution()
    print(me.longestCommonPrefix(["flower","flow","flight"]))