import copy
from dataclasses import dataclass

@dataclass
class Position(object):
    raw: str

    def is_empty(self):
        return self.raw == "L"

    def is_floor(self):
        return self.raw == "."

    def is_occupied(self):
        return self.raw == "#"

def get_lines(file_path):
    with open(file_path) as fh:
        values = []
        for line in map(lambda x: x.strip(), fh.readlines()):
                values.append([Position(position)  for position in line])
        return values

def count_occupied(grid):
    return sum([ 1 if x.is_occupied() else 0 for line in grid for x in line])

def same_state(grid, other_grid):
    return all([ value.raw == other_grid[lineidx][index].raw
        for (lineidx, line) in enumerate(grid)
        for (index, value) in enumerate(line)])

def is_out_grid(index, positions, grid):
    (row, col) = index
    max_row = len(grid)
    max_col = len(grid[max_row - 1])
    (row_offset, col_offset) = positions
    row_out = (row_offset + row) < 0 or (row_offset + row) >= max_row 
    col_out = (col_offset + col) < 0 or (col_offset + col) >= max_col
    return row_out or col_out 

def explore_adjacent(index, grid):
    """
    Y | Y | Y
    Y | X | Y
    Y | Y | Y
    Args:
        index (int): index for search
        grid (list): grid positions
    Returns: 
        value (str): new value position
    """
    exploring_indexes = [(-1, -1), (0, -1), (1, -1),
    (-1, 0), (1, 0,),
    (-1, 1), (0, 1), (1, 1)]
    (x, y) = index
    
    valid_indexes = list(filter(lambda position: not is_out_grid(index, position, grid), exploring_indexes))

    occupied_seats = [ grid[x + x_offset][y + y_offset].is_occupied() for (x_offset, y_offset) in valid_indexes]    
    all_not_occupied = all(map(lambda x: not x, occupied_seats))

    if  grid[x][y].is_empty() and all_not_occupied:
        return "#"

    if  grid[x][y].is_occupied() and occupied_seats.count(True) >= 4:
        return "L"
    
    return grid[x][y].raw

def run_iteration(grid):
    previous_state = copy.deepcopy(grid)
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            grid[x][y].raw = explore_adjacent((x,y), previous_state)
    return grid
    
def print_grid(grid):
    for line in grid:
        print("".join([ position.raw for position in line]))

example_grid = get_lines("day11/part1/iter0")
it1 = get_lines("day11/part1/iter1")
it2 = get_lines("day11/part1/iter2")
it3 = get_lines("day11/part1/iter3")
it4 = get_lines("day11/part1/iter4")
it5 = get_lines("day11/part1/iter5")

state1 = run_iteration(example_grid)
assert True == same_state(it1, state1)

state2 = run_iteration(state1)
assert True == same_state(it2, state2)

state3 = run_iteration(state2)
assert True == same_state(it3, state3)

state4 = run_iteration(state3)
assert True == same_state(it4, state4)

state5 = run_iteration(state4)
assert True == same_state(it5, state5)

state6 = run_iteration(state5)
assert True == same_state(it5, state6)

assert 37 == count_occupied(state6)

input_grid = get_lines("day11/input")

def compute_all(grid):
    previous_state = copy.deepcopy(grid)
    current_state = run_iteration(copy.deepcopy(grid))
    while not same_state(current_state, previous_state):
        previous_state = copy.deepcopy(current_state)
        current_state = run_iteration(copy.deepcopy(previous_state))
    return current_state

final_state = compute_all(input_grid)

print(f"Sol 1: {count_occupied(final_state)}")


def get_indexes(increment):
    return [(-increment, -increment), (0, -increment), (increment, -increment),
    (-increment, 0), (increment, 0,),
    (-increment, increment), (0, increment), (increment, increment)]

def explore_direction(grid, index, offset):
    (x, y) = index
    (x_o, y_o) = offset
    if x + x_o < 0 or y + y_o < 0:
        return False    
    try:
        position = grid[x + x_o][y + y_o]
        if position.is_empty():
            return False
    except IndexError:
        return False
    next_x = 0 if x_o == 0 else  (x_o + 1 if x_o > 0 else x_o - 1)
    next_y = 0 if y_o == 0 else  (y_o + 1 if y_o > 0 else y_o - 1)
    return position.is_occupied() or explore_direction(grid, index, (next_x, next_y))

def explore_adjacent(index, grid):
    """
    D1 | D2 | D3
    D4 | XX | D5
    D6 | D7 | D8
    Args:
        index (int): index for search
        grid (list): grid positions
    Returns: 
        value (str): new value position
    """
    (x, y) = index
    occupied_seats = [ 
        explore_direction(grid, index, (-1, -1)), # D1
        explore_direction(grid, index, (0, -1)), # D2
        explore_direction(grid, index, (1, -1)), # D3
        explore_direction(grid, index, (-1, 0)), # D4
        explore_direction(grid, index, (1, 0)), # D5
        explore_direction(grid, index, (-1, 1)), # D6
        explore_direction(grid, index, (0, 1)), # D7
        explore_direction(grid, index, (1, 1))  # D8
    ]    

    all_not_occupied = all(map(lambda x: not x, occupied_seats))

    if  grid[x][y].is_empty() and all_not_occupied:
        return "#"

    if  grid[x][y].is_occupied() and occupied_seats.count(True) >= 5:
        return "L"
    
    return grid[x][y].raw

example_grid = get_lines("day11/part2/iter0")

it1 = get_lines("day11/part2/iter1")
it2 = get_lines("day11/part2/iter2")
it3 = get_lines("day11/part2/iter3")
it4 = get_lines("day11/part2/iter4")
it5 = get_lines("day11/part2/iter5")

state1 = run_iteration(example_grid)
assert True == same_state(it1, state1)

state2 = run_iteration(state1)
assert True == same_state(it2, state2)

state3 = run_iteration(state2)
assert True == same_state(it3, state3)

state4 = run_iteration(state3)
assert True == same_state(it4, state4)

state5 = run_iteration(state4)
assert True == same_state(it5, state5)

state6 = run_iteration(state5)
assert 26 == count_occupied(state5)

final_state = compute_all(input_grid)

print(f"Sol 2: {count_occupied(final_state)}")