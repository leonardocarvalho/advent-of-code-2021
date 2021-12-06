def parse_line(line):
    direction, value = line.split()
    return (direction, int(value))


with open("input.txt") as f:
    moves = [parse_line(line) for line in f.readlines()]


depth = 0
horizontal = 0
for direction, value in moves:
    if direction == "forward": horizontal += value
    if direction == "up": depth -= value
    if direction == "down": depth += value

print(depth, horizontal, depth * horizontal)


aim = 0
depth = 0
horizontal = 0
for direction, value in moves:
    if direction == "forward":
        horizontal += value
        depth += aim * value
    if direction == "up": aim -= value
    if direction == "down": aim += value

print(depth, horizontal, aim, depth * horizontal)
