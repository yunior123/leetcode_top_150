class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }

        count = 0

        for i, value in enumerate(s):
            if i == len(s)-1:
                break
            if roman_dict[value] < roman_dict[s[i + 1]]:
                count -= roman_dict[value] 
            else:
                count += roman_dict[value]

        return count + roman_dict[s[-1]]