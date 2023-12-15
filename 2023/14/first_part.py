import numpy as np


def triangle_number(n):
    return (n * (n + 1)) // 2


def triangle_diff(m, n):
    return triangle_number(n) - triangle_number(m)


def score_roll_right(row):
    blockers = [0] + list(np.flatnonzero(row == "#")) + [len(row)]
    s = 0
    for i in range(1, len(blockers)):
        rollers = np.count_nonzero(row[blockers[i - 1] : blockers[i]] == "O")
        s += triangle_diff(blockers[i] - rollers, blockers[i])
    return s


def main():
    with open("input.txt", encoding="utf-8") as file:
        data = np.array([np.array(list(line.rstrip())) for line in file.readlines()])
    print(sum(map(score_roll_right, np.fliplr(data.T))))


if __name__ == "__main__":
    main()
