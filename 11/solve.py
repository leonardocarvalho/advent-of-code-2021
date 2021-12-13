import itertools

with open("input.txt") as f:
    enegy_levels = [[int(c) for c in line.strip()] for line in f.readlines()]


def neighboors(x, y):
    for dx, dy in itertools.product([-1, 0, 1], [-1, 0, 1]):
        if (
                (dx != 0 or dy != 0) and
                (0 <= x + dx < len(enegy_levels[0])) and
                (0 <= y + dy < len(enegy_levels))
        ):
            yield x + dx, y + dy


def perform_step():
    flashed_in_step = set()
    queue = []
    for y in range(len(enegy_levels)):
        for x in range(len(enegy_levels[0])):
            enegy_levels[y][x] += 1
            if enegy_levels[y][x] > 9:
                queue.append((x, y))

    while queue:
        x, y = queue.pop()
        if (x, y) in flashed_in_step:
            continue
        flashed_in_step.add((x, y))
        for nx, ny in neighboors(x, y):
            enegy_levels[ny][nx] += 1
            if (nx, ny) not in flashed_in_step and enegy_levels[ny][nx] > 9:
                queue.append((nx, ny))

    for x, y in flashed_in_step:
        enegy_levels[y][x] = 0

    return flashed_in_step


total_flashes = 0
n_steps = 0
all_flashed = False
while True:
    flashed_in_step = perform_step()
    total_flashes += len(flashed_in_step)
    n_steps += 1
    if n_steps == 100:
        print("Part 1:", total_flashes)
    if not all_flashed and (len(flashed_in_step) == len(enegy_levels) * len(enegy_levels[0])):
        all_flashed = True
        print("Part 2:", n_steps)
    if all_flashed and n_steps >= 100:
        break
