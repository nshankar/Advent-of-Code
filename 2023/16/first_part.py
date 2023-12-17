import numpy as np

UP = np.array([-1, 0])
RIGHT = np.array([0, 1])
LEFT = np.array([0, -1])
DOWN = np.array([1, 0])
REFLECT = np.array([[0, 1], [1, 0]])


# Closures!
def initialize_helpers(data):
    m, n = len(data), len(data[0])

    def in_bounds(v):
        i, j = v
        return 0 <= i and i < m and 0 <= j and j < n

    def process_state(location, direction):
        if not in_bounds(location + direction):
            return None, []

        new_location = location + direction
        new_directions = []
        action = data[*new_location]

        if action == "/":
            new_directions.append(-REFLECT @ direction)
        elif action == "\\":
            new_directions.append(REFLECT @ direction)
        elif action == "|":
            if np.array_equal(direction, LEFT) or np.array_equal(direction, RIGHT):
                new_directions.extend([UP, DOWN])
            else:
                new_directions.append(direction)
        elif action == "-":
            if np.array_equal(direction, LEFT) or np.array_equal(direction, RIGHT):
                new_directions.append(direction)
            else:
                new_directions.extend([LEFT, RIGHT])
        else:
            new_directions.append(direction)

        return new_location, new_directions

    return process_state


def count_energized(starting_state, layout):
    process_state = initialize_helpers(layout)

    # contains (location, direction) pairs of beams
    beams = [starting_state]
    visited = set()
    while len(beams):
        location, direction = beams.pop()
        # print(location, direction)
        if (tuple(location), tuple(direction)) in visited:
            continue
        visited.add((tuple(location), tuple(direction)))
        new_location, new_directions = process_state(location, direction)
        for new_direction in new_directions:
            beams.append((new_location, new_direction))  # pyright: ignore

    return len(set([a for a, _ in visited])) - 1


def main():
    with open("input.txt", encoding="utf-8") as f:
        layout = np.array([np.array(list(line.rstrip())) for line in f.readlines()])

    print(count_energized((np.array([0, -1]), RIGHT), layout))


if __name__ == "__main__":
    main()
