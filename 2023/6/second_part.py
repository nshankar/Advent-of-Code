import numpy as np


def main():
    with open("input.txt", encoding="utf-8") as file:
        lines = file.readlines()
        time = int("".join(lines[0].split(":")[1].split()))
        record = int("".join(lines[1].split(":")[1].split()))
    # A nicer approach would be root finding
    t = np.arange(1, time)
    print(np.count_nonzero(t * (time - t) > record))


if __name__ == "__main__":
    main()
