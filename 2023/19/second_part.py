from math import prod

from first_part import parse_input


class OrderedPair(tuple):
    def __lt__(self, other):
        if isinstance(other, int):
            return self[1] <= other
        raise TypeError("Unsupported comparison")

    def __gt__(self, other):
        if isinstance(other, int):
            return self[0] > other
        raise TypeError("Unsupported comparison")

    def between(self, other):
        if isinstance(other, int):
            return self[0] < other and other < self[1] - 1
        raise TypeError("Unsupported comparison")


def pair_splitter(pair, splitter, offset=False):
    a, b = pair
    return (
        OrderedPair((a, splitter + int(offset))),
        OrderedPair((splitter + int(offset), b)),
    )


def dfs(state, part):
    if state in ["A", "R"]:
        counter[state] += prod(b - a for a, b in part.values())
        return
    x, m, a, s = part["x"], part["m"], part["a"], part["s"]  # noqa
    for condition, value in rules[state]:
        if eval(condition):
            dfs(value, part)
            break
        else:
            attr = condition[0]
            offset = condition[1] == ">"
            n = int(condition[2:])
            if part[attr].between(n):
                p, q = pair_splitter(part[attr], n, offset)
                lo_part, hi_part = part.copy(), part.copy()
                lo_part[attr], hi_part[attr] = p, q
                dfs(state, lo_part)
                dfs(state, hi_part)
                return


def main():
    v = OrderedPair((1, 4001))
    part = {k: v for k in ["x", "m", "a", "s"]}
    dfs("in", part)
    print(counter)


if __name__ == "__main__":
    with open("input.txt", encoding="utf-8") as f:
        rules, _ = parse_input(*f.read().split("\n\n"))
    counter = {"A": 0, "R": 0}
    main()
