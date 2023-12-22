import numpy as np
from queue import Queue
from numba import njit


# Closures!
def initialize_helpers(data):
    m, n = data.shape
    N = np.array((-1, 0))
    E = np.array((0, 1))
    W = np.array((0, -1))
    S = np.array((1, 0))

    def in_bounds(v):
        return (0 <= v[0] < m) and (0 <= v[1] < n)

    def get_valid_neighbors(x, visited):
        valid_neighbors = []
        grid_idx, point_idx = x
        for d in [N, E, W, S]:
            nbr = point_idx + d
            if in_bounds(nbr):
                if not visited[grid_idx][*nbr]:
                    valid_neighbors.append((grid_idx, nbr))
            else:
                nbr = np.mod(nbr, data.shape)  # bring in bounds
                if (nbr_grid_idx := tuple(np.array(grid_idx) + d)) not in visited:
                    visited[nbr_grid_idx] = data == "#"
                if not visited[nbr_grid_idx][*nbr]:
                    valid_neighbors.append((nbr_grid_idx, nbr))
        return valid_neighbors

    return get_valid_neighbors, in_bounds


@njit
def rest_of_sum(NN, N, q_lens, lag):
    s = 0
    anchors = q_lens[-lag:]
    deltas = np.zeros(11, dtype=np.int64)
    for i in range(lag):
        deltas[i] = q_lens[i - lag] - q_lens[i - 2 * lag]
    for i in range(NN - N):
        if (N + i + 1) % 2 == (NN % 2):
            s += anchors[i % lag]
            s += (i // lag + 1) * deltas[i % lag]
    return s


def main():
    with open("input.txt", encoding="utf-8") as file:
        data = np.array(
            [np.array(list(line.rstrip())) for line in file.readlines()], dtype=str
        )
    get_valid_neighbors, _ = initialize_helpers(data)

    N = 500
    NN = 26501365
    lag = 457 - 326  # from inspecting data
    q_lens = [0] * (N + 1)
    q = Queue()
    visited = {(0, 0): data == "#"}

    start = (0, 0), np.argwhere(data == "S")[0]
    q.put(start)
    visited[start[0]][*start[1]] = True
    for i in range(N + 1):
        q_lens[i] = q.qsize()
        new_q = Queue()
        while q.qsize():
            x = q.get()
            for nbr in get_valid_neighbors(x, visited):
                new_q.put(nbr)
                visited[nbr[0]][*nbr[1]] = True
        q = new_q

    s = sum(q_lens[NN % 2 :: 2])
    # use periodicitiy
    s += rest_of_sum(NN, N, np.array(q_lens, dtype=np.int64), lag)
    print(s)


if __name__ == "__main__":
    main()
