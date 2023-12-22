import numpy as np
from queue import Queue


# Closures!
def initialize_helpers(data):
    m, n = len(data), len(data[0])
    N = np.array((-1, 0))
    E = np.array((0, 1))
    W = np.array((0, -1))
    S = np.array((1, 0))

    def in_bounds(v):
        i, j = v
        return 0 <= i and i < m and 0 <= j and j < n

    def get_valid_neighbors(x, visited):
        valid_neighbors = []
        for d in [N, E, W, S]:
            if in_bounds(x + d) and data[*(x + d)] == "." and not visited[*(x + d)]:
                valid_neighbors.append(x + d)
        return valid_neighbors

    return get_valid_neighbors, in_bounds


def main():
    with open("input.txt", encoding="utf-8") as file:
        data = np.array(
            [np.array(list(line.rstrip())) for line in file.readlines()], dtype=str
        )
    get_valid_neighbors, _ = initialize_helpers(data)

    N = 64
    q_lens = [0] * (N + 1)
    q = Queue()
    visited = np.full(data.shape, False, dtype=np.bool_)

    start = np.argwhere(data == "S")[0]
    q.put(start)
    visited[*start] = True
    for i in range(N + 1):
        q_lens[i] = q.qsize()
        new_q = Queue()
        while q.qsize():
            x = q.get()
            for nbr in get_valid_neighbors(x, visited):
                new_q.put(nbr)
                visited[*nbr] = True
        q = new_q

    print(sum(q_lens[::2]))


if __name__ == "__main__":
    main()
