import numpy as np
import scipy.sparse as sp
from itertools import product


# Reuse from day 10
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


def my_indexer(idx, orig_shape, new_shape):
    return np.unravel_index(np.ravel_multi_index(idx, orig_shape), new_shape)


def initialize_graph(data):
    in_bounds, v_to_i, _ = initialize_helpers(data)
    # Custom shape to make indexing easier. We can pretend to work
    # with this shape while actually working with a 2d sparse matrix
    shape = (4, 4, 4, data.size, 4, 4, 4, data.size)
    G = sp.dok_matrix((4**3 * data.size, 4**3 * data.size), dtype=np.uint8)

    # Initialize graph
    for i, j in product(range(len(data)), range(len(data[0]))):
        vertex = np.array((i, j))
        v_idx = v_to_i(vertex)
        for k, direction in enumerate([N, E, S, W]):
            nbr = vertex + direction
            nbr_idx = v_to_i(nbr)
            if not in_bounds(nbr):
                continue
            for l, m, n in product(range(4), repeat=3):  # noqa
                # prevent 3 steps in the same direction
                # and prevent reversing directions
                if (l, m, n) == (k, k, k) or n == ((k + 2) % 4):
                    continue
                index = my_indexer((l, m, n, v_idx, m, n, k, nbr_idx), shape, G.shape)
                G[index] = data[*nbr]
    return G


def main():
    with open("input.txt", encoding="utf-8") as file:
        data = np.array([list(map(int, line.rstrip())) for line in file.readlines()])

    G = initialize_graph(data)
    dists = sp.csgraph.dijkstra(
        G,
        indices=list(range(0, 64 * data.size, data.size)),
        min_only=True,
    )
    print(min(dists[data.size - 1 :: data.size]))


if __name__ == "__main__":
    N = np.array((-1, 0))
    E = np.array((0, 1))
    W = np.array((0, -1))
    S = np.array((1, 0))
    main()
