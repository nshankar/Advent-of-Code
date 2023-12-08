from first_part import parse_nodes
from math import lcm


def iter_til_Z(state, directions, nodes):
    counter = 0
    while True:
        for dir in directions:
            state = nodes[state][int(dir)]
            counter += 1
            if state[-1] == "Z":
                return counter


def main():
    with open("input.txt", encoding="utf-8") as file:
        data = [line.strip() for line in file.readlines()]
    directions = data[0].replace("L", "0").replace("R", "1")
    nodes = {x[0]: (x[1], x[2]) for x in map(parse_nodes, data[2:])}

    """
    There is no principled reason this should work. We are simply blessed by multiple serendipities:
        Let ??A be our starting state and ??Z, n_steps = iter_til_Z(??A), then
        1. ??Z is the only node ending in 'Z' reachable from ??A
        2. len(directions) divides n_steps
        3. ??Z is reached infinitely many times with period n_steps

    What good luck to see such symmetry!
    """
    states = [node for node in nodes if node[-1] == "A"]
    print(lcm(*[iter_til_Z(state, directions, nodes) for state in states]))


if __name__ == "__main__":
    main()
