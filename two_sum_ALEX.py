def twoSum(nums, target):
    index_mem = []
    if sum(nums) == target:
        index_mem = [i for i in range(len(nums))]
    else:
        for x in range(len(nums) - 1):
            for y in range(x + 1, len(nums)):
                if nums[x] + nums[y] == target:
                    index_mem.append(x)
                    index_mem.append(y)
    return index_mem


print(twoSum([3, 2, 3], 6))
