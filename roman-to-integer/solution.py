numerals = {"I":1 , "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}

class Solution:
    def romanToInt(self, s:str) -> int:
        n = len(s)
        num = numerals[s[n-1]]
        
        for i in range(n-2 , -1, -1):
            print(i)
            if numerals[s[i]] >= numerals[s[i+1]]:
                num += numerals[s[i]]
            else:
                num -= numerals[s[i]]
        return num

    # def romanToInt(self, s: str) -> int:
    #     sums = 0
    #     i = 0
    #     while i < len(s) - 1:
    #         if numerals[s[i]] < numerals[s[i+1]]:
    #             sums += numerals[s[i+1]] - numerals[s[i]]
    #             i += 1
    #         else:
    #             sums += numerals[s[i]]
    #         i += 1
    #     if i != len(s):
    #         sums += numerals[s[-1]]

    #     return sums 

me = Solution()
print(me.romanToInt("MCMXCIV"))