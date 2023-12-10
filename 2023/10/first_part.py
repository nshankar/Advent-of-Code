import numpy as np
import scipy.sparse as sp


N = np.array((-1, 0))
E = np.array((0, 1))
W = np.array((0, -1))
S = np.array((1, 0))
START = "START"
parser = {
    "|": (N, S),
    "-": (E, W),
    "L": (N, E),
    "J": (N, W),
    "7": (S, W),
    "F": (S, E),
    ".": None,
    "S": START,
}


# Closures!
def initialize_helpers(data):
    m, n = len(data), len(data[0])

    def in_bounds(v):
        i, j = v
        return 0 <= i and i < m and 0 <= j and j < n

    def vertex_to_index(v):
        return v[0] * n + v[1]

    def index_to_vertex(k):
        return k // n, k % n

    return in_bounds, vertex_to_index, index_to_vertex


def initialize_graph(data):
    in_bounds, v_to_i, _ = initialize_helpers(data)
    n_vertices = len(data) * len(data[0])
    G = np.zeros((n_vertices, n_vertices), dtype=np.int64)

    # Initialize graph
    for i in range(len(data)):
        for j in range(len(data[i])):
            dirs = parser[data[i, j]]
            if dirs is None or dirs == START:
                continue

            vertex = np.array((i, j))
            for dir in dirs:
                if in_bounds(vertex + dir):
                    G[v_to_i(vertex), v_to_i(vertex + dir)] = 1

    start = np.argwhere(data == "S")[0]
    # Add edges out of start point
    for dir in [N, E, W, S]:
        # potential neighbor
        nbr = start + dir
        if not in_bounds(nbr) or parser[str(data[*nbr])] is None:
            continue
        if any(np.array_equal(-dir, x) for x in parser[str(data[*nbr])]):
            G[v_to_i(start), v_to_i(nbr)] = 1
    return sp.csr_matrix(G), v_to_i(start)


def main():
    with open("input.txt", encoding="utf-8") as file:
        data = np.array(
            [np.array(list(line.rstrip())) for line in file.readlines()], dtype=str
        )
    G, start = initialize_graph(data)
    dists = sp.csgraph.dijkstra(G, indices=(start))
    print(max(dists[dists < np.inf]))


if __name__ == "__main__":
    main()
