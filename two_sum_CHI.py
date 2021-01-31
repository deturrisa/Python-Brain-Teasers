# Two Sum problem

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

# Example
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Output: Because nums[0] + nums[1] == 9, we return [0, 1].

def two_sum(numbers, target):
    output = []
    for num in numbers:
        numbers_1 = numbers[:]
        numbers_1.remove(num)
        for num_1 in numbers_1:
            if len(output) == 0:
                if num + num_1 == target:
                    if num == num_1:
                        print(num)
                        print(num_1)
                        output.append([i for i, n in enumerate(numbers) if n == num][0])
                        output.append([i for i, n in enumerate(numbers) if n == num][1])
                    else:
                        output.append(numbers.index(num))
                        output.append(numbers.index(num_1))
            else:
                break
    return output


two_sum([4,11,15,1,8],9)
two_sum([4,11,15,5,4],9)
two_sum([1,4,1],2)
two_sum([1,1,1],2)
two_sum([4,5,4],9)
two_sum([4,5,15,1,8],16)
two_sum([5,5,15,1,8],10)
two_sum([1,2,5,1,5],10)
two_sum([3,2,4],6)


