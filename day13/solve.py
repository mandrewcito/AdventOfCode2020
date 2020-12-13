from dataclasses import dataclass
def get_lines(file_path):
    with open(file_path) as fh:
        lines = [ x.strip() for x in fh.readlines()]
        return BusService(int(lines[0]), [int(x) for x in lines[1].split(",") if x != "x"], [x for x in lines[1].split(",")])

@dataclass
class BusService(object):
    first_timestamp: int
    buses: list
    buses_raw: list

example_input = get_lines("day13/example")

problem_input = get_lines("day13/input")

def get_bus(example_input):
    time = example_input.first_timestamp
    can_take = any(map(lambda bus: time % bus == 0, example_input.buses))
    while not can_take:
        time +=1        
        can_take = any(map(lambda bus: time % bus == 0, example_input.buses))
    buses = list(filter(lambda x: time % x == 0, example_input.buses))
    return (time - example_input.first_timestamp) * buses[0] 

assert 295 == get_bus(example_input)

print(f"Sol 1: {get_bus(problem_input)}")


def earliest_timestamp(buses_raw):
    buses = list(map(int, filter(lambda x: x!= "x", buses_raw)))
    modules = [-i % int(v) for i, v in enumerate(buses_raw) if v !='x']
    timestamp = 0
    step = 1
    for bus, mod in zip(buses, modules):
        while timestamp % bus != mod:
            timestamp += step
        step *= bus
    return timestamp

assert 1068781 == earliest_timestamp(example_input.buses_raw)

print(f"Sol 2: {earliest_timestamp(problem_input.buses_raw)}")
