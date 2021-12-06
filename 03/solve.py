import collections
import functools


def to_int(bits):
    return functools.reduce(lambda acc, v: 2 * acc + int(v), bits, 0)


with open("input.txt") as f:
    data = [list(l.strip()) for l in f.readlines()]


transpose = list(zip(*data))
gama_bits = [collections.Counter(col).most_common()[0][0] for col in transpose]
gama = to_int(gama_bits)
epsilon = to_int(['0' if bit == '1' else '1' for bit in gama_bits])

print(gama, epsilon, gama * epsilon)


def filter_gas(data, default, is_reversed):
    index = 0
    while len(data) > 1:
        transpose = list(zip(*data))
        most_common_data = collections.Counter(transpose[index]).most_common()
        priority_data = (
            most_common_data if not is_reversed else
            list(reversed(most_common_data))
        )
        (pri_elem, pri_value), (low_pri_elem, low_pri_value) = priority_data
        if pri_value == low_pri_value:
            elem = default
        else:
            elem = pri_elem

        data = [d for d in data if d[index] == elem]
        index += 1

    return data[0]


oxygen = to_int(filter_gas(data[:], '1', False))
co2 = to_int(filter_gas(data[:], '0', True))

print(oxygen, co2, oxygen * co2)
