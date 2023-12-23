import numpy as np
import scipy.sparse as sp
from itertools import product

from first_part import initialize_helpers, my_indexer


def initialize_graph(data):
    in_bounds, v_to_i, _ = initialize_helpers(data)
    # Custom shape to make indexing easier. We can pretend to work
    # with this shape while actually working with a 2d sparse matrix
    shape = (4, 11, data.size, 4, 11, data.size)
    G = sp.dok_matrix((4 * 11 * data.size, 4 * 11 * data.size), dtype=np.uint8)

    for i, j in product(range(len(data)), range(len(data[0]))):
        vertex = np.array((i, j))
        v_idx = v_to_i(vertex)
        for k, l in product(range(4), repeat=2):  # noqa
            prev_direction, direction = NEWS[k], NEWS[l]
            # No U-turns
            if np.array_equal(direction, -prev_direction):
                continue
            for prev_momentum in range(4, 11):
                if np.array_equal(direction, prev_direction):
                    momentum = prev_momentum + 1
                else:
                    momentum = 4

                # special case, invalid
                if momentum == 11:
                    continue

                # special case, just turned must travel 4
                if momentum == 4:
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

                if l in [1, 3]:
                    left, right = vertex, nbr
                else:
                    left, right = nbr, vertex
                G[index] = (
                    np.sum(data[left[0] : right[0] + 1, left[1] : right[1] + 1])
                    - data[*vertex]
                )
    return G


def main():
    with open("input.txt", encoding="utf-8") as file:
        data = np.array([list(map(int, line.rstrip())) for line in file.readlines()])

    print("initializing...")
    G = initialize_graph(data)
    print("solving...")
    dists = sp.csgraph.dijkstra(
        G,
        indices=list(range(0, 4 * 11 * data.size, data.size)),
        min_only=True,
        directed=True,
    )
    print("ans", min(dists[data.size - 1 :: data.size]))


if __name__ == "__main__":
    N = np.array((-1, 0))
    E = np.array((0, 1))
    W = np.array((0, -1))
    S = np.array((1, 0))
    NEWS = [N, E, W, S]
    main()
