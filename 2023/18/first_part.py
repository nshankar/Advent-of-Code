import numpy as np

directions = {
    "U": np.array((-1, 0)),
    "R": np.array((0, 1)),
    "L": np.array((0, -1)),
    "D": np.array((1, 0)),
}

get_symbol = {
    ("U", "U"): "|",
    ("D", "D"): "|",
    ("L", "L"): "-",
    ("R", "R"): "-",
    ("D", "R"): "L",
    ("L", "U"): "L",
    ("R", "U"): "J",
    ("D", "L"): "J",
    ("R", "D"): "7",
    ("U", "L"): "7",
    ("U", "R"): "F",
    ("L", "D"): "F",
}


def get_terrain_size(data):
    max_row, max_col = 0, 0
    min_row, min_col = 0, 0
    position = np.array([0, 0])
    for d, n in data:
        max_row = max(position[0], max_row)
        max_col = max(position[1], max_col)
        min_row = min(position[0], min_row)
        min_col = min(position[1], min_col)
        position += n * directions[d]
    return (
        max_row - min_row,
        max_col - min_col,
        np.array((-min_row, -min_col), dtype=np.int64),
    )


def main():
    with open("input.txt", encoding="utf-8") as file:

        def parse_line(line):
            d, n, _ = line.rstrip().split()
            return d, int(n)

        data = list(map(parse_line, file.readlines()))

    m, n, start = get_terrain_size(data)
    terrain = np.full((m + 1, n + 1), ".")  # pyright: ignore

    x = start
    for i, move in enumerate(data):
        d_s, n = move
        d = directions[d_s]
        for j in range(1, n):
            terrain[*(x + j * d)] = "|" if d[0] else "-"
        terrain[*(x + n * d)] = (
            get_symbol[d_s, data[i + 1][0]] if i + 1 < len(data) else "S"
        )
        x += n * d

    # Save and reuse day 10 on output.txt
    np.savetxt("output.txt", terrain, fmt="%s", delimiter="")


if __name__ == "__main__":
    main()
