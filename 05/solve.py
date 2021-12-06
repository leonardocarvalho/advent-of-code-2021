import collections
import math


with open("input.txt") as f:
    lines = [
        [list(map(int, point.split(','))) for point in line.split(" -> ")]
        for line in f.readlines()
    ]


def produce_integer_points_vert_or_hor_line(line):
    p1, p2 = line
    x1, y1 = p1
    x2, y2 = p2
    if x1 == x2:
        return [(x1, y) for y in range(min(y1, y2), max(y1, y2) + 1)]
    if y1 == y2:
        return [(x, y1) for x in range(min(x1, x2), max(x1, x2) + 1)]
    return []


def produce_integer_points(line):
    p1, p2 = line
    x1, y1 = p1
    x2, y2 = p2

    if y1 == y2 or x1 == x2:
        return produce_integer_points_vert_or_hor_line(line)

    dx = x2 - x1
    dy = y2 - y1
    gcd = math.gcd(dx, dy)
    dx = int(dx / gcd)
    dy = int(dy / gcd)

    off_by_one = 1 if x2 > x1 else -1
    return [
        (x, int(y1 + dy / dx * (x - x1)))
        for x in range(x1, x2 + off_by_one, dx)
    ]


# Part 1
passing_lines_counter = collections.Counter([
    point for line in lines
    for point in produce_integer_points_vert_or_hor_line(line)
])
print("Total point with more than two lines: {}".format(sum(
    1 for v in passing_lines_counter.values() if v > 1
)))


# Part 2
passing_lines_counter = collections.Counter([
    point for line in lines for point in produce_integer_points(line)
])
print("Total point with more than two lines: {}".format(sum(
    1 for v in passing_lines_counter.values() if v > 1
)))
