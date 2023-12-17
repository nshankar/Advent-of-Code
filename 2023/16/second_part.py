import numpy as np
from first_part import count_energized


def main():
    with open("input.txt", encoding="utf-8") as f:
        layout = np.array([np.array(list(line.rstrip())) for line in f.readlines()])
    m, n = len(layout), len(layout[0])

    starting_states = (
        [(np.array([i, -1]), RIGHT) for i in range(m)]
        + [(np.array([-1, j]), DOWN) for j in range(n)]
        + [(np.array([i, 0]), LEFT) for i in range(m)]
        + [(np.array([0, j]), UP) for j in range(n)]
    )

    max_energy = 0
    for starting_state in starting_states:
        max_energy = max(max_energy, count_energized(starting_state, layout))

    print(max_energy)


if __name__ == "__main__":
    UP = np.array([-1, 0])
    RIGHT = np.array([0, 1])
    LEFT = np.array([0, -1])
    DOWN = np.array([1, 0])
    REFLECT = np.array([[0, 1], [1, 0]])
    main()
