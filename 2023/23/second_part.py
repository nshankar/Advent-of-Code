import numpy as np
from collections import defaultdict
from itertools import product

slopes = {
    "^": np.array((-1, 0)),
    ">": np.array((0, 1)),
    "v": np.array((1, 0)),
    "<": np.array((0, -1)),
}


def in_bounds(x):
    return 0 <= x[0] < data.shape[0] and 0 <= x[1] < data.shape[1]


def get_valid_neighbors(pos):
    valid_neighbors = []
    for d in slopes.values():  # hacky
        nbr = np.array(pos) + d
        if in_bounds(nbr) and data[*nbr] != "#":
            valid_neighbors.append(tuple(nbr))
    return valid_neighbors


def calculate_path_length(path, graph):
    s = 0
    for i in range(len(path) - 1):
        v, w = path[i], path[i + 1]
        assert graph[(v, w)] == graph[(w, v)]
        s += graph[(v, w)]
    return s


def dfs(pos, end, path, graph, adj_list):
    # path is a dict since dicts remember input order
    if pos == end:
        paths.append(calculate_path_length(list(path.keys()) + [pos], graph))
        if len(paths) % 1000 == 1:
            print(max(paths))
    if pos in path:
        return
    path[pos] = True
    for nbr in adj_list[pos]:
        dfs(nbr, end, path.copy(), graph, adj_list)


def get_vertices(start, end):
    vertices = set([start, end])
    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] != "#" and len(get_valid_neighbors(np.array((i, j)))) > 2:
                vertices.add((i, j))
    return vertices


def fill_nbr_weights(start, ends, graph):
    stack = [(start, set([start]))]
    while stack:
        pos, visited = stack.pop()
        if pos != start and pos in ends:
            graph[(start, pos)] = max(len(visited), graph[(start, pos)])
            continue

        visited.add(pos)
        for nbr in get_valid_neighbors(pos):
            if nbr not in visited:
                stack.append((nbr, visited.copy()))


def get_adjacency_list(graph, vertices):
    adj_list = defaultdict(list)
    for v, w in product(vertices, repeat=2):
        if (v, w) in graph:
            adj_list[v].append(w)
    return adj_list


def main():
    start, end = (0, 1), (140, 139)  # look at data
    # start, end = (0, 1), (22, 21)  # look at data

    vertices = get_vertices(start, end)
    graph = defaultdict(int)
    for v in vertices:
        fill_nbr_weights(v, vertices, graph)
    adj_list = get_adjacency_list(graph, vertices)
    dfs(start, end, {}, graph, adj_list)
    print(max(paths))


if __name__ == "__main__":
    with open("input.txt", encoding="utf-8") as file:
        data = np.array(
            [np.array(list(line)) for line in file.read().splitlines()], dtype=str
        )
    paths = []
    main()
