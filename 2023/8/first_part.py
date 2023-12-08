import re


def parse_nodes(line):
    match = re.search(r"(\w+)\s*=\s*\((\w+),\s*(\w+)\)", line)
    if match:
        return match.groups()


def main():
    with open("input.txt", encoding="utf-8") as file:
        data = [line.strip() for line in file.readlines()]
    directions = data[0].replace("L", "0").replace("R", "1")
    nodes = {x[0]: (x[1], x[2]) for x in map(parse_nodes, data[2:])}

    state = "AAA"
    counter = 0
    while True:
        for dir in directions:
            state = nodes[state][int(dir)]
            counter += 1
            if state == "ZZZ":
                print(counter)
                return


if __name__ == "__main__":
    main()
