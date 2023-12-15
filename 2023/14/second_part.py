import numpy as np
from numba import njit

# Converting to bytes
OSCAR = ord("O")  # 79
SHARP = ord("#")  # 35
DOT = ord(".")  # 46


@njit()
def simulate_roll_right(row):
    blockers = np.append(np.flatnonzero(row == SHARP), len(row))
    rollers = np.count_nonzero(row[0 : blockers[0]] == OSCAR)
    row[0 : blockers[0] - rollers] = DOT
    row[blockers[0] - rollers : blockers[0]] = OSCAR
    for i in range(1, len(blockers)):
        lo, hi = blockers[i - 1] + 1, blockers[i]
        rollers = np.count_nonzero(row[lo:hi] == OSCAR)
        row[lo : hi - rollers] = DOT
        row[hi - rollers : hi] = OSCAR
    return row


def cycle(data):
    m, n = data.shape
    # roll north
    for j in range(n):
        data[:, j] = simulate_roll_right(data[:, j][::-1])[::-1]
    # roll west
    for i in range(m):
        data[i, :] = simulate_roll_right(data[i, :][::-1])[::-1]
    # roll south
    for j in range(n):
        data[:, j] = simulate_roll_right(data[:, j])
    # roll east
    for i in range(m):
        data[i, :] = simulate_roll_right(data[i, :])
    return data


def score(data):
    n = len(data[0])
    return np.arange(n, 0, -1, dtype=np.int64) @ np.count_nonzero(data == OSCAR, axis=1)


def find_period(arr):
    for x in range(2, len(arr) // 2 + 1):
        # start at end of array since leading values can be misleading
        if np.array_equal(arr[-1 - x : -1], arr[-1 - 2 * x : -1 - x]):
            return x
    return 1


def main():
    with open("input.txt", encoding="utf-8") as file:
        # Converting to bytes
        data = np.array(
            [
                np.array([ord(char) for char in line.rstrip()], dtype=np.uint8)
                for line in file.readlines()
            ],
            dtype=np.uint8,
        )

    N = 500
    scores = np.empty(N, dtype=np.int64)
    for i in range(N):
        data = cycle(data)
        scores[i] = score(data)

    p = find_period(scores)
    idx = ((10**9 - N) % p) - p + N - 1
    print("Period:", p, "Final score:", scores[idx])


if __name__ == "__main__":
    main()
