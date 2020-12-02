def get_lines():
    with open("day02/input") as fh:
        return [ line.strip() for line in fh.readlines()]


def split_line(line):
    requirements, password = line.split(":")
    requirements, letter = requirements.split(" ")
    minimum, maximum = requirements.split("-")
    return int(minimum), int(maximum), letter, password.strip()

def check_line(line):
    minimum, maximum, letter, password = split_line(line)
    return minimum <= password.count(letter) <= maximum

lines = get_lines()

filtered = list(filter(check_line, lines))
print(len(filtered))

def check_line_positions(line):
    lower, upper, letter, password = split_line(line)
    return (password[lower - 1] == letter) ^ (password[upper - 1] == letter)

filtered = list(filter(check_line_positions, lines))
print(len(filtered))