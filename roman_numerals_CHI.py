
class Solution(object):
    def romanToInt(self,s):
        dict = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000,
            'IV':4,
            'IX':9,
            'XL':40,
            'XC':90,
            'CD':400,
            'CM':900
        }

        romans = [x for x in s]
        output = 0
        i = 0
        while len(romans) > 0:
            try:
                if romans[i] + romans[i + 1] in dict:
                    output += dict[romans[i] + romans[i + 1]]
                    romans.remove(romans[i])
                    romans.remove(romans[i])
                else:
                    output += dict[romans[i]]
                    romans.remove(romans[i])
            except:
                output += dict[romans[i]]
                romans.remove(romans[i])

        return output


solution = Solution()
result = solution.romanToInt("CMLXXXVIII")
print(result)

