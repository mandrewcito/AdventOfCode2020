from functools import reduce

def get_lines(file_path):
    with open(file_path) as fh:
        return [ line.strip() for line in fh.readlines()]

example_lines = get_lines("day03/example")

input_lines = get_lines("day03/input")

left_offset = 3

offset = 0

SQUARE = "."
TREE = "#"

squares = 0 # O
trees = 0 # X


def check_line(line, x_offset, y_offset):
    index = x_offset % len(line)
    #print(line)
    items = list(line)
    if line[index] == SQUARE:
        items[index] = "O"
        line = "".join(items)
        return 1, 0
    elif line[index] == TREE:
        items[index] = "X"
        line = "".join(items)
        return 0, 1
    else:
        raise ValueError("PLUM !")
    #print(line)

def create_dict(x_step, y_step):
    return {
        "trees": 0,
        "squares": 0,
        "x_offset": x_step,
        "y_offset": y_step,
        "x_step": x_step,
        "y_step": y_step
    }

def sum_amount(step_name, line, amount, line_number):
    if amount[step_name]["y_step"] == 2 and line_number % 2 == 0:
        return
    squares, trees = check_line(line, amount[step_name]["x_offset"], amount[step_name]["y_offset"])
    amount[step_name]["squares"] = amount[step_name]["squares"]  + squares
    amount[step_name]["trees"] = amount[step_name]["trees"]  + trees
    amount[step_name]["x_offset"] = amount[step_name]["x_offset"] + amount[step_name]["x_step"]
    amount[step_name]["y_offset"] = amount[step_name]["y_offset"] + amount[step_name]["y_step"]    

def process_file(lines):
    amount = {
        "r1d1": create_dict(1, 1),
        "r3d1": create_dict(3, 1),
        "r5d1": create_dict(5, 1),
        "r7d1": create_dict(7, 1),
        "r1d2": create_dict(1, 2)
        
    } 
    for index, line in enumerate(lines):
        sum_amount("r3d1", line, amount, index)
        sum_amount("r1d1", line, amount, index)
        sum_amount("r5d1", line, amount, index)
        sum_amount("r7d1", line, amount, index)
        sum_amount("r1d2", line, amount, index)   
    #print(amount)
    trees = list(map(lambda x: x["trees"], amount.values()))
    print(trees)
    print(reduce(lambda z, y: z * y , trees))

print("1:-------------- Test")
process_file(example_lines[1:])

print("2:-------------- Input")
process_file(input_lines[1:])


