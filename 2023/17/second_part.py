import numpy as np
import scipy.sparse as sp
from itertools import product

from first_part import initialize_helpers, my_indexer


def initialize_graph(data):
    in_bounds, v_to_i, _ = initialize_helpers(data)
    # Custom shape to make indexing easier. We can pretend to work
    # with this shape while actually working with a 2d sparse matrix
    shape = (4, 7, data.size, 4, 7, data.size)
    G = sp.dok_matrix((4 * 7 * data.size, 4 * 7 * data.size), dtype=np.uint8)

    for i, j in product(range(len(data)), range(len(data[0]))):
        vertex = np.array((i, j))
        v_idx = v_to_i(vertex)
        for k, l in product(range(4), repeat=2):  # noqa
            prev_direction, direction = NEWS[k], NEWS[l]
            # No U-turns
            if np.array_equal(direction, -prev_direction):
                continue
            for prev_momentum in range(7):
                if np.array_equal(direction, prev_direction):
                    momentum = prev_momentum + 1
                else:
                    momentum = 0

                # special case, must turn
                if momentum > 6:
                    continue

                # special case must travel 4
                if momentum == 0:
                    nbr = vertex + 4 * direction
                else:
                    nbr = vertex + direction
                if not in_bounds(nbr):
                    continue

                nbr_idx = v_to_i(nbr)
                index = my_indexer(
                    (
                        k,
                        prev_momentum,
                        v_idx,
                        l,
                        momentum,
                        nbr_idx,
                    ),
                    shape,
                    G.shape,
                )
                G[index] = (
                    np.sum(data[vertex[0] : nbr[0] + 1, vertex[1] : nbr[1] + 1])
                    - data[*vertex]
                )
    return G


def main():
    with open("test3.txt", encoding="utf-8") as file:
        data = np.array([list(map(int, line.rstrip())) for line in file.readlines()])

    print("initializing...")
    # data = data[:10, :13]
    G = initialize_graph(data)
    print("solving...")
    # starting_indices = list(range(3, 4 * 7 * data.size, data.size))
    dists = sp.csgraph.dijkstra(
        G,
        indices=list(
            range(0, 4 * 7 * data.size, data.size)
        ),  # [0, 14 * data.size],  # North, 0 momentum, 0 and West, 0 momentum, 0
        min_only=True,
        directed=True,
    )
    for dist in set(dists[data.size - 1 :: data.size]):
        print(dist)
    print(min(dists[data.size - 1 :: data.size]))


if __name__ == "__main__":
    N = np.array((-1, 0))
    E = np.array((0, 1))
    W = np.array((0, -1))
    S = np.array((1, 0))
    NEWS = [N, E, W, S]
    main()
