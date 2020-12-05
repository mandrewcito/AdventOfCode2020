range_left = lambda sit_range: sit_range[0: round(len(sit_range) / 2)] 
range_right = lambda sit_range: sit_range[round(len(sit_range) / 2):]


def map_sit(boarding_pass, row, sit_range):
    if len(boarding_pass) == 0:
        return row[0], sit_range[0]
    letter = boarding_pass[0]
    if letter == "L":
        return map_sit(boarding_pass[1:], row, range_left(sit_range))
    elif letter == "R":
        return map_sit(boarding_pass[1:], row, range_right(sit_range))

def map_sit_row(boarding_pass, sit_range):
    letter = boarding_pass[0]
    if letter == "F":
        return map_sit_row(boarding_pass[1:], range_left(sit_range))
    elif letter == "B":
        return map_sit_row(boarding_pass[1:], range_right(sit_range))
    else:
        return map_sit(boarding_pass, sit_range, get_columns())

get_columns = lambda: list(range(0,8))
get_sits = lambda: list(range(0, 127))
get_row_column = lambda boarding_pass: map_sit_row(boarding_pass, get_sits())

#print(get_row_column("FBFBBFFRLR"))
assert  get_row_column("FBFBBFFRLR") == (44, 5)


assert  map_sit_row("BFFFBBFRRR", range(0, 127)) == (70, 7)
assert  map_sit_row("FFFBBBFRRR", range(0, 127)) == (14, 7)
assert  map_sit_row("BBFFBBFRLL", range(0, 127)) == (102, 4)

def get_id(boarding_pass):
    row, column = map_sit_row(boarding_pass, range(0, 127))
    return (row * 8 + column)

assert get_id("BFFFBBFRRR") == 567
assert get_id("FFFBBBFRRR") == 119
assert get_id("BBFFBBFRLL")== 820

ids = [get_id(boarding_pass.strip()) for boarding_pass in open("day05/input").readlines()]

print(f" Sol 1: {max(ids)}")
print(len(get_sits()[1:-1]))
print(len(get_columns()[1:-1]))
all_ids = [(row * 8 + column) for column in get_columns() for row in get_sits()]
print(len(ids), len(all_ids))

print([x for x in all_ids if x not in ids and x + 1 in ids and x - 1 in ids])