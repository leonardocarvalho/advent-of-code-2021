import functools
import itertools


def parse_line(line):
    raw_digits, raw_output = line.split(" | ")
    return {
        "digits": raw_digits.strip().split(" "),
        "output": raw_output.strip().split(" "),
    }


with open("input.txt") as f:
    logs = [parse_line(line) for line in f.readlines()]


print("Part 1:", sum([
    sum(1 for entry in log["output"] if len(entry) in {2, 4, 3, 7})
    for log in logs
]))


DIGITS = {
    0: {'a', 'b', 'c', 'e', 'f', 'g'},
    1: {'c', 'f'},
    2: {'a', 'c', 'd', 'e', 'g'},
    3: {'a', 'c', 'd', 'f', 'g'},
    4: {'b', 'c', 'd', 'f'},
    5: {'a', 'b', 'd', 'f', 'g'},
    6: {'a', 'b', 'd', 'e', 'f', 'g'},
    7: {'a', 'c', 'f'},
    8: {'a', 'b', 'c', 'd', 'e', 'f', 'g'},
    9: {'a', 'b', 'c', 'd', 'f', 'g'},
}
all_digits = {'a', 'b', 'c', 'd', 'e', 'f', 'g'}


def compute_output_value(output, fake_to_actual):

    def to_actual_value(fake_digit):
        actual_digit = {fake_to_actual[c] for c in fake_digit}
        for digit, rep in DIGITS.items():
            if actual_digit == rep:
                return digit
        raise Exception

    return functools.reduce(lambda acc, v: 10 * acc + v, [
        to_actual_value(fake_digit)
        for fake_digit in output
    ], 0)


def compute_output(log):
    actual_to_fake = {}

    fixed_len = [(1, 2), (4, 4), (7, 3)]
    reps = {
        digit: set(next(entry for entry in log["digits"] if len(entry) == length))
        for digit, length in fixed_len
    }

    actual_to_fake['a'], = list(reps[7] - reps[1])
    # '6' has length six and its intersection is a single element.
    # Others with length six has intersecition two.
    reps[6], = [
        set(entry)
        for entry in log["digits"]
        if len(entry) == 6 and len(set(entry) & set(reps[1])) == 1
    ]
    actual_to_fake['c'], = list(reps[1] - reps[6])  # 6 contains f
    actual_to_fake['f'], = list(reps[1] - {actual_to_fake['c']})

    # Only '3' has length five and contains c and f
    reps[3], = [
        set(entry) for entry in log["digits"]
        if len(entry) == 5 and actual_to_fake['c'] in entry and actual_to_fake['f'] in entry
    ]
    # Intersection between 3 and 4 excluding c and f is d
    actual_to_fake['d'], = list(reps[3] & reps[4] - {actual_to_fake['c'], actual_to_fake['f']})

    actual_to_fake['b'], = list(reps[4] - {actual_to_fake['c'],
                                           actual_to_fake['d'],
                                           actual_to_fake['f']})

    actual_to_fake['g'], = list(reps[3] - {actual_to_fake['a'],
                                           actual_to_fake['c'],
                                           actual_to_fake['d'],
                                           actual_to_fake['f']})

    actual_to_fake['e'], = list(all_digits - set(actual_to_fake.values()))

    fake_to_actual = {v: k for k, v in actual_to_fake.items()}
    return compute_output_value(log["output"], fake_to_actual)


def compute_brute_force(log):

    def is_possible_solution(fake_to_actual):
        return all(
            {fake_to_actual[c] for c in digit} in DIGITS.values()
            for digit in log["digits"]
        )

    for perm in itertools.permutations(all_digits):
        fake_to_actual = dict(zip(sorted(all_digits), perm))
        if is_possible_solution(fake_to_actual):
            return compute_output_value(log["output"], fake_to_actual)
    raise Exception


print("Part 2:", sum(compute_output(log) for log in logs))
print("Part 2.2 (brute force it):", sum(compute_brute_force(log) for log in logs))
