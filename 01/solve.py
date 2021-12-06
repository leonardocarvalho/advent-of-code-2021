with open("input.txt") as f:
    data = list(map(int, f.readlines()))

# Part 1
print(sum(p < n for p, n in zip(data[:-1], data[1:])))


# Part 2
s = data[0] + data[1] + data[2]
increases = 0
for index in range(3, len(data)):
    ls = s
    s = ls + data[index] - data[index - 3]
    increases += s > ls
print(increases)
