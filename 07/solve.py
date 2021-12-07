import math

with open("input.txt") as f:
    positions = sorted(list(map(int, f.readline().strip().split(","))))


# Part 1
# The minimum fuel cost happens when the position is the median.
# Considering the sorted array, let's compare the fuel cost of picking the median to choosing a
# value V greater than the median M. The fuel delta is:
#   (# smaller values then V) * (V - M) - (# greater values then V) * (V - M) > 0
# So more fuel is spent. Picking a smaller value than the median is analogous.
# If array size is even pick either of the median yield the same result (because the
# displacement of either median to the other is the same)
center = int(math.floor(len(positions) / 2))
spent_fuel = sum(abs(v - positions[center]) for v in positions)
print("Part 1:", spent_fuel)


# Part 2
def compute_fuel_cost(positions, destination):
    return sum(abs(destination - p) * (abs(destination - p) + 1) / 2 for p in positions)

min_fuel_cost = min(
    compute_fuel_cost(positions, p) for p in range(min(positions), max(positions) + 1)
)
print("Part 2:", min_fuel_cost)
