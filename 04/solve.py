def parse_board(lines):
    data = [list(map(int, l.replace('  ', ' ').split(' '))) for l in lines]
    return {
        "rows": list(map(set, data)) + list(map(set, zip(*data))),
        "all_numbers": set(number for l in data for number in l)
    }


with open("input.txt") as f:
    input_lines = [l.strip() for l in f.readlines()]

    draws = list(map(int, input_lines[0].split(',')))
    boards = [
        parse_board(input_lines[i:i + 5])
        for i in range(2, len(input_lines), 6)
    ]


def is_winner(board, drawn_set):
    return any(drawn_set.issuperset(row) for row in board["rows"])


def compute_score(board, drawn_set, last_draw):
    return sum(board["all_numbers"] - drawn_set) * last_draw


# Part 1
for n_drawn in range(1, len(draws) + 1):
    drawn_set = set(draws[:n_drawn])
    last_draw = draws[n_drawn - 1]
    winner = next((b for b in boards if is_winner(b, drawn_set)), None)
    if winner:
        print("Board wins first. Score: {}".format(
            compute_score(winner, drawn_set, last_draw)
        ))
        break


# Part 2
not_winners = boards[:]
for n_drawn in range(1, len(draws) + 1):
    drawn_set = set(draws[:n_drawn])
    last_draw = draws[n_drawn - 1]
    prev = not_winners[:]
    not_winners = [b for b in not_winners if not is_winner(b, drawn_set)]
    if len(not_winners) == 0:
        print("Last to win score: {}".format(
            compute_score(prev[0], drawn_set, last_draw)
        ))
        break
