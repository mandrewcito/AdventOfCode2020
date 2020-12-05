range_left = lambda seat_range: seat_range[0: round(len(seat_range) / 2)] 
range_right = lambda seat_range: seat_range[round(len(seat_range) / 2):]


def map_seat(boarding_pass, row, seat_range):
    if len(boarding_pass) == 0:
        return row[0], seat_range[0]
    letter = boarding_pass[0]
    if letter == "L":
        return map_seat(boarding_pass[1:], row, range_left(seat_range))
    elif letter == "R":
        return map_seat(boarding_pass[1:], row, range_right(seat_range))

def map_seat_row(boarding_pass, seat_range):
    letter = boarding_pass[0]
    if letter == "F":
        return map_seat_row(boarding_pass[1:], range_left(seat_range))
    elif letter == "B":
        return map_seat_row(boarding_pass[1:], range_right(seat_range))
    else:
        return map_seat(boarding_pass, seat_range, get_columns())

get_columns = lambda: list(range(0,8))
get_rows = lambda: list(range(0, 127))
get_row_column = lambda boarding_pass: map_seat_row(boarding_pass, get_rows())

#print(get_row_column("FBFBBFFRLR"))
assert  get_row_column("FBFBBFFRLR") == (44, 5)


assert  map_seat_row("BFFFBBFRRR", range(0, 127)) == (70, 7)
assert  map_seat_row("FFFBBBFRRR", range(0, 127)) == (14, 7)
assert  map_seat_row("BBFFBBFRLL", range(0, 127)) == (102, 4)

def get_id(boarding_pass):
    row, column = map_seat_row(boarding_pass, range(0, 127))
    return (row * 8 + column)

assert get_id("BFFFBBFRRR") == 567
assert get_id("FFFBBBFRRR") == 119
assert get_id("BBFFBBFRLL")== 820

ids = [get_id(boarding_pass.strip()) for boarding_pass in open("day05/input").readlines()]

print(f"Sol 1: {max(ids)}")

all_ids = [(row * 8 + column) for column in get_columns() for row in get_rows()]

empty_seats = [x for x in all_ids if x not in ids and x + 1 in ids and x - 1 in ids]
print(f"Sol 2: {empty_seats}")