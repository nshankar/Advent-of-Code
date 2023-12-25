from itertools import chain
import igraph as ig


def parse_line(line):
    key = line.split(": ")[0]
    vals = line.split(": ")[1].split(" ")
    return key, vals


def main():
    with open("input.txt", encoding="utf-8") as f:
        data = [parse_line(line) for line in f.read().splitlines()]

    keys = set([data[i][0] for i in range(len(data))]) | set(
        chain.from_iterable([data[i][1] for i in range(len(data))])
    )
    key_to_index = {k: i for i, k in enumerate(keys)}

    n = len(keys)
    graph = ig.Graph(n, directed=False)  # Assuming a directed graph
    for key, vals in data:
        for v in vals:
            graph.add_edge(key_to_index[key], key_to_index[v])

    print(graph.mincut())


if __name__ == "__main__":
    main()
