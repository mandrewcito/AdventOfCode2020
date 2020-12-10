import collections
from dataclasses import dataclass

@dataclass
class Adapter(object):
    output_joltage: int

    def diff(self, adapter):
        return self.output_joltage - adapter.output_joltage

def get_lines(file_path):
    with open(file_path) as fh:
        return [Adapter(int(x.strip())) for x in fh.readlines()]

def get_adapters(file_path):
    adapters = get_lines(file_path)
    max_adapter = Adapter(max(map(lambda adapter: adapter.output_joltage, adapters)) + 3)
    adapters.append(max_adapter)
    return adapters

example_input = get_adapters("day10/example")
example2_input = get_adapters("day10/example2")
problem_input = get_adapters("day10/input")

def get_jolt_diffs(adapters):
    data = collections.defaultdict(int)
    index = 1
    sorted_adapters = sorted(adapters, key=lambda x: x.output_joltage, reverse=False)
    data[sorted_adapters[0].output_joltage] = 1
    while index < len(sorted_adapters):
        diff = sorted_adapters[index].diff(sorted_adapters[index -1])
        data[diff] = data[diff] + 1
        index = index + 1

    return (data[1], data[2], data[3])

assert (7, 0, 5) == get_jolt_diffs(example_input)

assert (22, 0, 10) == get_jolt_diffs(example2_input)

diffs = get_jolt_diffs(problem_input)

print(f"Sol 1: {diffs[0] * diffs[2] }")

def get_jolts_paths(adapters):
    """example:
        input => [1, 4, 5, 6, 7, 10, 11, 12, 15, 16, 19, 22]
        idx(jolt) => (-1) + (-2) + (-3)
        
        1 => 1 + 0 + 0
        4 => 0 + 0 + 1
        5 => 1 + 0 + 0
        6 => 1 + 1 + 0
        7 => 2 + 1 + 1
        10 => 0 + 0 + 4
        11 => 4 + 0 + 0
        12 => 4 + 4 + 0
        15 => 0 + 0 + 8
        16 => 8 + 0 + 0
        19 => 0 + 0 + 8
        22 => 0 + 0 + 8

        data => defaultdict(<class 'int'>,
        {
            0: 1, -1: 0, -2: 0, 1: 1, 3: 0, 2: 0, 4: 1, 5: 1, 
            6: 2, 7: 4, 9: 0, 8: 0, 10: 4, 11: 4, 12: 8, 14: 0,
            13: 0, 15: 8, 16: 8, 18: 0, 17: 0, 19: 8, 21: 0, 20: 0,
            22: 8
        })
    Args:
        adapters (list): jolts list
       
    Returns:
        int: number of paths can be explored
    """
    print(list(map(lambda x: x.output_joltage, adapters)))
    data = collections.defaultdict(int)
    data[0] = 1
    for adapter in adapters: 
        print(f"{adapter.output_joltage} => {data[adapter.output_joltage-1]} + {data[adapter.output_joltage-2]} + {data[adapter.output_joltage-3]}")
        data[adapter.output_joltage] = data[adapter.output_joltage-1] + data[adapter.output_joltage-2] + data[adapter.output_joltage-3] 
    print(data)
    return data[adapters[-1].output_joltage]

def get_different_paths(adapters):
    sorted_adapters = sorted(
        adapters,
        key=lambda x: x.output_joltage,
        reverse=False)
    return get_jolts_paths(sorted_adapters)


assert 8 == get_different_paths(example_input)
assert 19208 == get_different_paths(example2_input)

print(f"Sol 2: {get_different_paths(problem_input)}")