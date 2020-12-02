def get_nums():
    with open("day01/input") as fh:
        return [ int(line.strip()) for line in fh.readlines()]

nums = get_nums()

any_sums = lambda x : list(filter(lambda number: x + number == 2020, nums))  
numbers = list(filter(lambda x: any_sums(x), nums))
print(numbers[0] * numbers[1])

any_sums_1 = lambda x: list(filter(lambda num: any_sums_2(x, num), nums))
any_sums_2 = lambda x, y : list(filter(lambda number: x + y + number == 2020, nums))   
numbers = list(filter(lambda x: any_sums_1(x), nums))
print(numbers[0] * numbers[1] * numbers[2])