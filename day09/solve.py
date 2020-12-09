import random

def get_lines(file_path):
    with open(file_path) as fh:
        return [int(x.strip()) for x in fh.readlines()]

example_input = get_lines("day09/example")
problem_input = get_lines("day09/input")

def number_matches_any(number, previous_numbers):
    for x in range(len(previous_numbers)):
        for y in range(len(previous_numbers)):
            if previous_numbers[x] == previous_numbers[y]:
                continue
            if previous_numbers[x] + previous_numbers[y] == number:
                return True
    return False

def get_number_preamble(numbers, index, preamble):
    test_numbers = numbers[index - preamble: index]
    number = numbers[index]
    return number, test_numbers


assert (6, [1, 2, 3, 4, 5]) == get_number_preamble([1, 2, 3, 4, 5, 6, 7, 8, 9], 5, 5)

def search_first(numbers, preamble, return_sum=False):
    index = preamble
    while index < len(numbers):
        number, test_numbers = get_number_preamble(numbers, index, preamble)
        if not number_matches_any(number, test_numbers):
            print(f"{number} , not sum in {test_numbers}")
            return number
        index = index + 1 

sample = list(range(1, 26))
random.shuffle(sample)

assert True == number_matches_any(26, sample)
assert True == number_matches_any(49, sample)
assert False == number_matches_any(100, sample)
assert False == number_matches_any(50, sample)

assert  True == number_matches_any(26, list(range(1, 20)) + list(range(21, 26)) + [45] )
assert  False == number_matches_any(65, list(range(1, 20)) + list(range(21, 26)) + [45] )
assert  True == number_matches_any(64, list(range(1, 20)) + list(range(21, 26)) + [45] )
assert  True == number_matches_any(66, list(range(1, 20)) + list(range(21, 26)) + [45] )

assert 127 == search_first(example_input, 5)

print( f"Sol 1: {search_first(problem_input, 25)}")

def calc_min_max(number, numbers):
    for x in range(len(numbers)):
        for y in range(len(numbers)):
            contigous_numbers =numbers[x:y] 
            if number == sum(contigous_numbers):
                return min(contigous_numbers), max(contigous_numbers)
    return False

def get_min_max(numbers, preamble):
    index = preamble
    while index < len(numbers):
        number, test_numbers = get_number_preamble(numbers, index, preamble)
        if not number_matches_any(number, test_numbers):
            return calc_min_max(number, numbers)
        index = index + 1 

min_ex, max_ex = get_min_max(example_input, 5)

assert (15, 47) == (min_ex, max_ex)
assert 62 == min_ex + max_ex

x, y = get_min_max(problem_input, 25)

print( f"Sol 2: {x + y }")
