import math

from dataclasses import dataclass


class Instruction(object):
    def __init__(self, line):
        self.action = line[0]
        self.value = int(line[1:])

class Ferry(object):
    """
    Action N means to move north by the given value.
    Action S means to move south by the given value.
    Action E means to move east by the given value.
    Action W means to move west by the given value.
    Action L means to turn left the given number of degrees.
    Action R means to turn right the given number of degrees.
    Action F means to move forward by the given value in the direction the ship is currently facing.
    Args:
        object ([type]): [description]
    """
    x: int = 0
    y: int = 0
    degree_offset: int = 0 # starts facing east
    
    def position(self):
        return (self.x, self.y)
    actions = {
        "N": (0, 1),
        "S": (0, -1),
        "E": (1, 0),
        "W": (-1, 0),
        "F": (0, 0)
    }
    
    def move(self, instruction: Instruction):
        (x, y) = self.actions[instruction.action]

        if instruction.action == "F":
            (x, y) = round(math.cos(math.radians(self.degree_offset))), round(math.sin(math.radians(self.degree_offset)))

        self.x = self.x + (x * instruction.value)
        self.y = self.y + (y * instruction.value)
            

    
    def rotate(self, degrees):
        self.degree_offset = (self.degree_offset + degrees) % 360

    def process_instruction(self, instruction: Instruction):
        if instruction.action in ["L", "R"]:
            self.rotate(instruction.value * (1 if instruction.action == "L" else -1))
        else:       
            self.move(instruction)    
    
    def manhattan(self, position):
        (x, y) = position
        return abs(self.x - x) + abs(self.y - y)

    def navigate(self, instructions: list):
        for instruction in instructions:
            self.process_instruction(instruction)


def get_lines(file_path):
    with open(file_path) as fh:
        return [Instruction(x.strip()) for x in fh.readlines()]


example_instructions = get_lines("day12/example")

problem_instructions = get_lines("day12/input")

ferry = Ferry()

ferry.process_instruction(example_instructions[0])

assert (10, 0) == ferry.position()

ferry.process_instruction(example_instructions[1])
assert (10, 3) == ferry.position()

ferry.process_instruction(example_instructions[2])
assert (17, 3) == ferry.position()

ferry.process_instruction(example_instructions[3])
assert (17, 3) == ferry.position()

ferry.process_instruction(example_instructions[4])
assert (17, -8) == ferry.position()

assert 25 == ferry.manhattan((0, 0))

ferry = Ferry()
ferry.navigate(problem_instructions)
print(f"Sol 1: {ferry.manhattan((0, 0))}")

class WaypointFerry(Ferry):
    waypoint = (10, 1) # (x, y)

    def process_instruction(self, instruction: Instruction):
        if instruction.action in ["L", "R"]:
            self.rotate(instruction.value * (1 if instruction.action == "L" else -1))
        elif instruction.action in ["N", "S", "E", "W"]:
            self.move_waypoint(instruction)
        else:
            self.move(instruction)    

    def move_waypoint(self, instruction):
        action = instruction.action
        if action == "N": # x, y + value
            self.waypoint = (self.waypoint[0], self.waypoint[1] + instruction.value)
        if action == "S": # x, y - value
            self.waypoint = (self.waypoint[0], self.waypoint[1] - instruction.value)
        if action == "W": # x + value, y 
            self.waypoint = (self.waypoint[0] - instruction.value, self.waypoint[1])
        if action == "E": # x - value, y 
            self.waypoint = (self.waypoint[0] + instruction.value, self.waypoint[1])

    def rotate(self, degrees):
        rotation = 0
        increment = 90 * ( 1 if degrees > 0 else -1)
        while degrees != rotation:
            self.waypoint = (1 if degrees < 0 else - 1) * self.waypoint[1], (-1 if degrees < 0 else 1) * self.waypoint[0]
            rotation += increment


    def move(self, instruction):
        if instruction.action == "F":
            self.x, self.y =   self.x + (instruction.value * self.waypoint[0]), self.y + (instruction.value * self.waypoint[1])
    

ferry = WaypointFerry()

ferry.process_instruction(example_instructions[0])

assert (100, 10) == ferry.position()

ferry.process_instruction(example_instructions[1])
assert (100, 10) == ferry.position()
assert (10, 4) == ferry.waypoint

ferry.process_instruction(example_instructions[2])
assert (170, 38) == ferry.position()
assert (10, 4) == ferry.waypoint

ferry.process_instruction(example_instructions[3])
assert (170, 38) == ferry.position()
assert (4, -10) == ferry.waypoint

ferry.process_instruction(example_instructions[4])
assert (214,-72) == ferry.position()
assert (4, -10) == ferry.waypoint

assert 286 == ferry.manhattan((0, 0))

ferry = WaypointFerry()
ferry.navigate(problem_instructions)
print(f"Sol 2: {ferry.manhattan((0, 0))}")