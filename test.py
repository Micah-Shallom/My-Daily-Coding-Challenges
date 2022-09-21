class Solution:
    numerals = {"I":1 , "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}

    def romanToInteger(self, s: str) -> int :
        n = len(s)
        num = self.numerals[s[n-1]]  
        
        for i in range(n-2, -1, -1):
            if self.numerals[s[i]] >= self.numerals[s[i+1]]:
                num += self.numerals[s[i]]
            else: 
                num -= self.numerals[s[i]]
        return num

me = Solution()
print(me.romanToInteger('MCMXCIV'))