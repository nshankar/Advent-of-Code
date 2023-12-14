import numpy as np
from first_part import process_patch


def find_smudge_horizontal(arr):
    n = len(arr[0])
    for col in range(1, n):
        width = min(col, n - col)
        lhs, rhs = max(0, col - width), min(n, col + width)
        if 1 == np.count_nonzero(arr[:, lhs:col] != np.fliplr(arr[:, col:rhs])):
            return col


def main():
    with open("input.txt", encoding="utf-8") as file:
        patches = file.read().strip().split("\n\n")
    data = [process_patch(patch) == "#" for patch in patches]

    s = 0
    for arr in data:
        f = find_smudge_horizontal
        s += f(arr) if f(arr) else 100 * f(arr.T)
    print(s)


if __name__ == "__main__":
    main()
