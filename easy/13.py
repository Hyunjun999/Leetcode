class Solution:
    def romanToInt(self, s: str) -> int:
        d = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900,
        }
        res, ptr = 0, 0
        while ptr < len(s):
            if s[ptr] in ["I", "X", "C"]:
                if ptr + 1 < len(s):
                    if s[ptr] + s[ptr + 1] in d:
                        res += d[s[ptr] + s[ptr + 1]]
                        ptr += 2
                    else:
                        res += d[s[ptr]]
                        ptr += 1
                else:
                    res += d[s[ptr]]
                    ptr += 1
            else:
                res += d[s[ptr]]
                ptr += 1
        return res


# Given a roman numeral, convert it to an integer with some constraints:
# 'I' can be placed before V (5) and X (10) to make 4 and 9.
# 'X' can be placed before L (50) and C (100) to make 40 and 90.
# 'C' can be placed before D (500) and M (1000) to make 400 and 900.

sol = Solution()
assert sol.romanToInt("III") == 3
assert sol.romanToInt("LVIII") == 58
assert sol.romanToInt("MCMXCIV") == 1994
