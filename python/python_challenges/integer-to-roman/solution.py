class Solution:
    def intToRoman(self, num: int) -> str:
        map_table = {
            1:      "I",
            5:      "V",
            10:     "X",
            50:     "L",
            100:    "C",
            500:    "D",
            1000:   "M",
            4:      "IV",
            9:      "IX",
            40:     "XL",
            90:     "XC",
            400:    "CD",
            900:    "CM",
        }

        roman = ""

        while num:
            if num == 0:
                return roman
            if num in map_table:
                return roman + map_table[num]

            base_value = 0
            for value in map_table:
                if base_value < value < num:
                    base_value = value
            roman += ((num // base_value) * map_table[base_value])
            num = num % base_value
        return roman

me = Solution()
print(me.intToRoman(7))