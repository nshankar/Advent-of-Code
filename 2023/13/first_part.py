import numpy as np


def process_patch(s):
    rows = s.split("\n")
    return np.array([np.array(list(row)) for row in rows], dtype=str)


def find_horizontal_reflection(arr):
    n = len(arr[0])
    for col in range(1, n):
        width = min(col, n - col)
        lhs, rhs = max(0, col - width), min(n, col + width)
        if np.array_equal(arr[:, lhs:col], np.fliplr(arr[:, col:rhs])):
            return col


def main():
    with open("input.txt", encoding="utf-8") as file:
        patches = file.read().strip().split("\n\n")
    data = [process_patch(patch) for patch in patches]

    s = 0
    for arr in data:
        f = find_horizontal_reflection
        s += f(arr) if f(arr) else 100 * f(arr.T)
    print(s)


if __name__ == "__main__":
    main()
