import collections


paths = collections.defaultdict(list)
with open("input.txt") as f:
    for line in f.readlines():
        cave1, cave2 = line.strip().split("-")
        for source, destination in ((cave1, cave2), (cave2, cave1)):
            if destination != "start":
                paths[source].append(destination)


# The input seems not to have two big caves connected. If there were big caves connected
# we would have to avoid make the same transition A -> B (for example) twice or we would have
# an infinite length path
def explore(
        root,
        path_so_far,
        reach_end_paths,
        visit_one_small_cave_twice=False,
        small_cave_visited_twice=None
):
    for cave in paths[root]:
        if cave == "end":
            reach_end_paths.append(path_so_far + ["end"])
            continue

        is_repeated_small_cave = cave.lower() == cave and cave in path_so_far
        if is_repeated_small_cave:
            if not visit_one_small_cave_twice or small_cave_visited_twice is not None:
                continue

        explore(
            cave,
            path_so_far + [cave],
            reach_end_paths,
            visit_one_small_cave_twice,
            small_cave_visited_twice=cave if is_repeated_small_cave else small_cave_visited_twice
        )


reach_end_paths = []
explore("start", [], reach_end_paths)
print("Part 1:", len(reach_end_paths))
reach_end_paths = []
explore("start", [], reach_end_paths, visit_one_small_cave_twice=True)
print("Part 2:", len(reach_end_paths))
