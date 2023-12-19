from intervaltree import IntervalTree

from first_part import get_terrain_size, directions


def parse_line(line):
    parse_numerical_direction = {
        0: "R",
        1: "D",
        2: "L",
        3: "U",
    }
    s = line.rstrip().split()[-1][2:-1]
    return parse_numerical_direction[int(s[-1])], int(s[:-1], 16)


def main():
    with open("input.txt", encoding="utf-8") as file:
        data = list(map(parse_line, file.readlines()))

    n_rows, _, start = get_terrain_size(data)

    down_tree = IntervalTree()
    up_tree = IntervalTree()

    x = start
    left_perimeter = 1
    for d, n in data:
        if d == "U":
            up_tree.addi(begin=x[0] - n, end=x[0], data=x[1])
        elif d == "D":
            down_tree.addi(begin=x[0], end=x[0] + n, data=x[1])
        elif d == "L":
            left_perimeter += n
        x += n * directions[d]

    area = 0
    for i in range(n_rows):
        up_points = [data[2] for data in up_tree[i]]
        down_points = [data[2] for data in down_tree[i]]
        area += sum(
            [abs(u - d) + 1 for u, d in zip(sorted(up_points), sorted(down_points))]
        )
    print(area, "+", left_perimeter, "=", area + left_perimeter)


if __name__ == "__main__":
    main()
