import math


with open("input.txt") as f:
    heightmap = [[int(v) for v in line.strip()] for line in f.readlines()]


def neighboors(x, y):
    for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
        if 0 <= x + dx < len(heightmap[0]) and 0 <= y + dy < len(heightmap):
            yield x + dx, y + dy


low_points = [
    (x, y, heightmap[y][x])
    for y in range(len(heightmap))
    for x in range(len(heightmap[0]))
    if all(heightmap[ny][nx] > heightmap[y][x] for nx, ny in neighboors(x, y))
]


def compute_basin_size(x, y, visited=None):
    if heightmap[y][x] == 9:
        return 0
    if visited is None:
        visited = [[False for a in range(len(heightmap[0]))] for b in range(len(heightmap))]
    if visited[y][x]:
        return 0
    visited[y][x] = True
    return 1 + sum(compute_basin_size(nx, ny, visited) for nx, ny in neighboors(x, y))


print("Part 1:", sum(l + 1 for _, _, l in low_points))
print("Part 2:", math.prod(sorted(compute_basin_size(x, y) for x, y, _ in low_points)[-3:]))
