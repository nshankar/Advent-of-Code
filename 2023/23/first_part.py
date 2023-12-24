import numpy as np

slopes = {
    "^": np.array((-1, 0)),
    ">": np.array((0, 1)),
    "v": np.array((1, 0)),
    "<": np.array((0, -1)),
}


def in_bounds(x):
    return np.all(np.zeros(2) <= x) and np.all(x < data.shape)


def get_valid_neighbors(pos, visited):
    # Uncomment for Part 1 solution
    # if data[*pos] in slopes:
    #     return [pos + slopes[data[*pos]]]  # pyright: ignore

    valid_neighbors = []
    for d in slopes.values():  # hacky
        nbr = pos + d
        if in_bounds(nbr) and data[*nbr] != "#" and tuple(nbr) not in visited:
            valid_neighbors.append(nbr)
    return valid_neighbors


#
# def dfs(pos, visited):
#     if np.array_equal(pos, end):
#         paths.append(len(visited))
#     if tuple(pos) in visited:
#         return
#
#     visited.add(tuple(pos))
#     for nbr in get_valid_neighbors(pos, visited):
#         dfs(nbr, visited.copy())
#


def dfs_non_recursive(start, end):
    stack = [(start, set([tuple(start)]))]

    while stack:
        pos, visited = stack.pop()
        if np.array_equal(pos, end):
            paths.append(len(visited) - 1)
            print(paths)
            continue

        for nbr in get_valid_neighbors(pos, visited):
            nbr_tuple = tuple(nbr)
            if nbr_tuple not in visited:
                new_visited = visited.copy()
                new_visited.add(nbr_tuple)
                stack.append((nbr, new_visited))


def main():
    dfs_non_recursive(start, end)
    print(paths)
    print(max(paths))


if __name__ == "__main__":
    with open("test.txt", encoding="utf-8") as file:
        data = np.array(
            [np.array(list(line)) for line in file.read().splitlines()], dtype=str
        )
    print(np.count_nonzero((data != "#") & (data != ".")))
    # start, end = np.array([0, 1]), np.array([140, 139])  # look at data
    start, end = np.array([0, 1]), np.array([22, 21])  # look at data
    paths = []
    main()
