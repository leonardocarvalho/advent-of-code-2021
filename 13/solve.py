fold_operations = []
dots = set()


with open("input.txt") as f:
    for line in [l.strip() for l in f.readlines()]:
        if not line:
            continue
        if "fold along" in line:
            direction, position = line[len("fold along "):].split("=")
            fold_operations.append({"direction": direction, "position": int(position)})
        else:
            x, y = line.split(",")
            dots.add((int(x), int(y)))


def dot_after_fold(dot, operation):
    if operation["direction"] == "y" and dot[1] > operation["position"]:
        return (dot[0], (- dot[1]) % operation["position"])
    if operation["direction"] == "x" and dot[0] > operation["position"]:
        return ((- dot[0]) % operation["position"], dot[1])
    return dot


def perform_fold(dots, operation):
    return {dot_after_fold(dot, operation) for dot in dots}


new_dots = perform_fold(dots, fold_operations[0])
print("Part 1:", len(new_dots))

final_dots = dots
for operation in fold_operations:
    final_dots = perform_fold(final_dots, operation)
max_x = max(d[0] for d in final_dots)
max_y = max(d[1] for d in final_dots)


for y in range(max_y + 1):
    print("".join(['#' if (x, y) in final_dots else '.' for x in range(max_x + 1)]))
