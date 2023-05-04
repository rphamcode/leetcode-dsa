class Solution:
    def roman_to_integer(self, s: str) -> int:
        # initialize roman dictionary 
        roman = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000,
            "IV" : 4,
            "IX" : 9,
            "XL" : 40,
            "XC" : 90,
            "CD" : 400,
            "CM" : 900
        }

        # initialize total and i
        total = 0
        i = 0

        # iterate through s
        while i < len(s):
            # if s[i:i + 2] is in roman, add roman[s[i:i + 2]] to total and increment i by 2
            if i < len(s) - 1 and s[i:i + 2] in roman:
                total += roman[s[i:i + 2]]
                i += 2
            # else, add roman[s[i]] to total and increment i by 1
            else:
                total += roman[s[i]]
                i += 1

        # return total
        return total

solution = Solution()
print(solution.roman_to_integer("LVIII"))