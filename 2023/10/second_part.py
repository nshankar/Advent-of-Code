import numpy as np
import scipy.sparse as sp
from first_part import initialize_helpers, initialize_graph


def is_northy(idx, path):
    return path[(idx + 1) % len(path)][0] - path[idx - 1][0] < 0


def is_southy(idx, path):
    return path[(idx + 1) % len(path)][0] - path[idx - 1][0] > 0


def get_direction(i, path):
    if is_northy(i, path):
        return 1
    elif is_southy(i, path):
        return -1
    return 0


def main():
    with open("input.txt", encoding="utf-8") as file:
        data = np.array(
            [np.array(list(line.rstrip())) for line in file.readlines()], dtype=str
        )
    _, _, i_to_v = initialize_helpers(data)
    G, start = initialize_graph(data)

    # DFS to orient the loop
    raw_dfs, _ = sp.csgraph.depth_first_order(G, i_start=start)
    dfs = list(map(i_to_v, raw_dfs))
    # map from points on loop to their orientation
    loop_map = {dfs[i]: get_direction(i, dfs) for i in range(len(dfs))}

    count = 0
    inside = False
    for i in range(len(data)):
        loop_dir = 0
        for j in range(len(data[i])):
            idx = (i, j)
            if loop_map.get(idx) is None:
                if inside:
                    count += 1
                continue
            # As we parse each line check if first intersection
            # with the loop is northy or southy. Use this to
            # distinguish the inside and outside
            if loop_dir == 0 and loop_map[idx]:
                loop_dir = loop_map[idx]
            inside = loop_map[idx] == loop_dir

    print(count)


if __name__ == "__main__":
    main()
