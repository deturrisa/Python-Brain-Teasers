class Solution(object):
    def intToRoman(self,s):
        dict_1 = {1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V', 6: 'VI', 7: 'VII', 8: 'VIII', 9: 'IX'}
        dict_2 = {1: 'X', 2: 'XX', 3: 'XXX', 4: 'XL', 5: 'L', 6: 'LX', 7: 'LXX', 8: 'LXXX', 9: 'XC'}
        dict_3 = {1: 'C', 2: 'CC', 3: 'CCC', 4: 'CD', 5: 'D', 6: 'DC', 7: 'DCC', 8: 'DCCC', 9: 'CM'}
        dict_4 = {1: 'M', 2: 'MM', 3: 'MMM'}

        dicts = {1: dict_1, 2: dict_2, 3: dict_3, 4: dict_4}

        nums = [x for x in str(s)]
        length = len(nums)
        output = ''

        for num in nums:
            if num == '0':
                pass
            else:
                output += dicts[length].get(int(num))
            length -= 1

        return output


solution = Solution()
solution.intToRoman(3458)


