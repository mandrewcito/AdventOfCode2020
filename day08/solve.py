import re
import copy
from dataclasses import dataclass
from functools import reduce

@dataclass
class Instruction(object):
    name: str
    value: int
    visited: bool = False
    
    def is_nop(self):
        return "nop" == self.name
    
    def is_jump(self):
        return "jmp" == self.name
    def is_acc(self):
        return "acc" == self.name

def get_lines(file_path):
    with open(file_path) as fh:
        return [Instruction(
            name=re.findall(r"(\w+) ([+-]\d+)", x.strip())[0][0],
            value=int(re.findall(r"(\w+) ([+-]\d+)", x.strip())[0][1]))  for x in fh.readlines()]

example_file = get_lines("day08/example")

input_file = get_lines("day08/input")


def run_instructions(instructions):
    acc = 0
    index = 0
    instruction = instructions[index]
    while not instruction.visited:
        if instruction.is_jump():
            index = index + instruction.value
        elif instruction.is_acc():
            acc = acc + instruction.value
            index = index + 1
        elif instruction.is_nop():
            index = index + 1
        instruction.visited = True

        if  index >= len(instructions):
            return acc
        instruction = instructions[index]
    return acc

assert 5 == run_instructions(example_file)

print(f"Sol 1: {run_instructions(input_file)}")

example_file2 = get_lines("day08/example2")

def check_path(index, instructions):
    instruction = instructions[index]
    try:
        while not instruction.visited:
            if instruction.is_jump():
                index = index + instruction.value
            elif instruction.is_acc():
                index = index + 1
            elif instruction.is_nop():
                index = index + 1
            instruction.visited = True
            instruction = instructions[index]
    except Exception as ex:
        print(ex)
        return index == len(instructions)
    return all(map(lambda x: x.visited, instructions))

def check(instruction_name, index, instructions):
    modified_path = copy.deepcopy(instructions)
    modified_path[index].name = instruction_name
    return check_path(index, modified_path), modified_path

def clean(instructions):
    for instruction in instructions:
        instruction.visited = False
    return instructions

def fix_program(instructions):
    index = 0
    original = copy.deepcopy(instructions)
    instruction = instructions[index]
    while not instruction.visited:
        if instruction.name == "jmp":
            result, path = check("nop", index, instructions)
            if result:
                return run_instructions(clean(path))

        if instruction.is_jump():
            index = index + instruction.value
        elif instruction.is_acc():
            index = index + 1
        elif instruction.is_nop():
            index = index + 1
        instruction.visited = True
        instruction = instructions[index]
    return run_instructions(original)

assert 8 == fix_program(example_file2)

print(f"Sol 2: {fix_program(clean(input_file))}")