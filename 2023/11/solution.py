import numpy as np
from itertools import combinations

# part 1
GALAXY_GROWTH_FACTOR = 1
# part 2
# GALAXY_GROWTH_FACTOR = 1000000 - 1


def count_in_interval(items, interval):
    a, b = interval
    return sum([1 for it in items if (a < it and it < b)])


def main():
    with open("input.txt", encoding="utf-8") as file:
        data = np.array([np.array(list(line)[:-1]) for line in file.readlines()])

    galaxies = np.argwhere(data == "#")
    cols_without_galaxies = np.flatnonzero(np.all(data == ".", axis=0))
    rows_without_galaxies = np.flatnonzero(np.all(data == ".", axis=1))

    dist = 0
    for g, h in combinations(galaxies, 2):
        dist += abs(g[0] - h[0]) + GALAXY_GROWTH_FACTOR * count_in_interval(
            rows_without_galaxies, (min(g[0], h[0]), max(g[0], h[0]))
        )
        dist += abs(g[1] - h[1]) + GALAXY_GROWTH_FACTOR * count_in_interval(
            cols_without_galaxies, (min(g[1], h[1]), max(g[1], h[1]))
        )
    print(dist)


if __name__ == "__main__":
    main()
