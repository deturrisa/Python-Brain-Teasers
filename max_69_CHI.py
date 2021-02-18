
class Solution:
    def maximum69Number(self, input):

        nums = [num for num in str(input)]

        for i in range(0, len(nums)):
            if nums[i] == '6':
                nums[i] = '9'
                break

        return int(''.join(nums))

obj = Solution()


obj.maximum69Number(9669)