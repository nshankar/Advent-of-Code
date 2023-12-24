import numpy as np
from itertools import combinations

L = 200000000000000
U = 400000000000000


def str_to_arr(s, coercer=int):
    return np.array(tuple(map(coercer, s.split(", "))))


def find_line_intersection(h, g):
    (x1, y1), (vx1, vy1) = h
    (x2, y2), (vx2, vy2) = g

    a1, b1, c1 = vx1, -vy1, vy1 * x1 - vx1 * y1
    a2, b2, c2 = vx2, -vy2, vy2 * x2 - vx2 * y2

    if a1 * b2 - b1 * a2 == 0:
        # Luckily no coincident paths
        return None

    A = np.array([[a1, b1], [a2, b2]])
    B = np.array([-c1, -c2])
    y, x = np.linalg.solve(A, B)
    return x, y


def in_bounds(x):
    return (L <= x[0] <= U) and (L <= x[1] <= U)


def in_future(h, g, x):
    hx, hv = h
    gx, gv = g
    h_future = np.sign(x[0] - hx[0]) == np.sign(hv[0])
    g_future = np.sign(x[0] - gx[0]) == np.sign(gv[0])
    return h_future and g_future


def main():
    with open("input.txt", encoding="utf-8") as f:
        hail = [
            tuple(map(lambda s: str_to_arr(s)[:2], line.split(" @ ")))
            for line in f.read().splitlines()
        ]
    s = 0
    for h, g in combinations(hail, r=2):
        x = find_line_intersection(h, g)
        if x is not None and in_bounds(x) and in_future(h, g, x):
            s += 1
    print(s)


if __name__ == "__main__":
    main()
