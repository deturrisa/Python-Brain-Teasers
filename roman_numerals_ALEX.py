roman_numerals = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

class Solution(object):
    def romanToInt(self, s):
        result = 0
        if len(s) == 0:
            return result
        if len(s) > 1:
            if self.isSpecial(s):
                return roman_numerals[s[1]] - roman_numerals[s[0]] + self.romanToInt(s[2:])
            else:
                result += roman_numerals[s[0]] + self.romanToInt(s[1:])
                return result
        result += roman_numerals[s[0]]
        return result


    def isSpecial(self, s):
        list_dic = list(roman_numerals)
        char_index = list_dic.index(s[0])
        if char_index < 5:
            return s[1] == list_dic[char_index + 1] or s[1] == list_dic[char_index + 2]

solution = Solution()
result = solution.romanToInt("IV")
print(result)