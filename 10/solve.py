import functools

class Corrupted(Exception):

    def __init__(self, char):
        self.char = char


push_pop_map = {"(": ")", "[": "]", "{": "}", "<": ">"}
push_chars = set(push_pop_map.keys())
pop_chars = set(push_pop_map.values())
error_score = {")": 3, "]": 57, "}": 1197, ">": 25137}
incomplete_score = {")": 1, "]": 2, "}": 3, ">": 4}


with open("input.txt") as f:
    lines = [line.strip() for line in f.readlines()]
    for line in lines:  # Input consistency
        assert len(set(line) - push_chars - pop_chars) == 0


def parse_line(line):
    current_push_char = line[0]
    assert current_push_char in push_chars  # Invariant
    remaining = line[1:]

    if remaining == "":  # Incomplete
        return "", [push_pop_map[current_push_char]]
    while remaining[0] in push_chars:
        remaining, missing_closing_chars = parse_line(remaining)
        if remaining == "":  # Incomplete
            return "", missing_closing_chars + [push_pop_map[current_push_char]]

    if remaining[0] == push_pop_map[current_push_char]:
        return remaining[1:], []
    raise Corrupted(remaining[0])


total_error_score = 0
incomplete_scores_list = []
for line in lines:
    try:
        if not line:
            continue
        if line[0] not in push_chars:
            raise Corrupted(line[0])
        _, missing_closing_chars = parse_line(line)
        if missing_closing_chars:
            incomplete_scores_list.append(functools.reduce(
                lambda acc, v: 5 * acc + v,
                [incomplete_score[c] for c in missing_closing_chars],
                0
            ))
    except Corrupted as e:
        total_error_score += error_score[e.char]


print("Part 1:", total_error_score)
print("Part 2:", sorted(incomplete_scores_list)[len(incomplete_scores_list) // 2])
