from collections import defaultdict
from functools import cmp_to_key
from itertools import product


def str_to_tuple(s, coercer=int):
    return tuple(map(coercer, s.split(",")))


def less_than(p, q):
    return p[2][1] < q[2][0]


def set_state(state, brick, val=True):
    for idx in brick_indices(brick):
        state[idx] = val
    return state


def get_state(state, brick):
    return [state[idx] for idx in brick_indices(brick)]


def brick_indices(brick):
    return product(*[range(dim[0], dim[1] + 1) for dim in brick])


def shift(brick, amount=-1):
    z0, z1 = brick[2]
    return (brick[0], brick[1], (z0 + amount, z1 + amount))


def squash(brick, direction=0):
    z = brick[2][direction]
    return (brick[0], brick[1], (z, z))


def underground(brick):
    return brick[2][0] <= 0


def settled(bricks, state):
    for brick in bricks:
        new_brick = shift(brick)
        if not underground(new_brick) and not any(get_state(state, squash(new_brick))):
            return False
    return True


def simulate_gravity(bricks):
    bricks = sorted(bricks, key=cmp_to_key(less_than))
    state = defaultdict(bool)

    # initialize state
    for brick in bricks:
        state = set_state(state, brick, True)

    # simulate
    falling_bricks = set()
    while not settled(bricks, state):
        for i, brick in enumerate(bricks):
            new_brick = shift(brick)
            if underground(new_brick) or any(get_state(state, squash(new_brick))):
                continue
            else:
                state = set_state(state, brick, False)
                state = set_state(state, new_brick, True)
                bricks[i] = new_brick
                falling_bricks.add(i)
    return bricks, state, len(falling_bricks)


def main():
    with open("input.txt", encoding="utf-8") as f:
        bricks = [
            tuple(zip(*tuple(map(str_to_tuple, line.split("~")))))
            for line in f.read().splitlines()
        ]

    bricks, state, _ = simulate_gravity(bricks)

    part_1, part_2 = 0, 0
    for brick in bricks:
        new_bricks = [other for other in bricks if other != brick]
        new_state = {k: v for k, v in state.items()}
        new_state = set_state(new_state, brick, False)

        _, _, counter = simulate_gravity(new_bricks)
        part_1 += not bool(counter)
        part_2 += counter
    print("Part 1:", part_1, "\nPart 2:", part_2)


if __name__ == "__main__":
    main()
