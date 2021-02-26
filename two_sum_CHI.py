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



