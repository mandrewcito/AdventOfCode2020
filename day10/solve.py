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
    data = collections.defaultdict(int)
    data[0] = 1
    for adapter in adapters: 
        data[adapter.output_joltage] = data[adapter.output_joltage-1] + data[adapter.output_joltage-2] + data[adapter.output_joltage-3] 
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