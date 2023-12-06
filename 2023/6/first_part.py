import numpy as np


def main():
    with open("input.txt", encoding="utf-8") as file:
        lines = file.readlines()
        times = map(int, lines[0].split(":")[1].split())
        records = map(int, lines[1].split(":")[1].split())

    margin_of_error = 1
    for (
        time,
        record,
    ) in zip(times, records):
        t = np.arange(1, time)
        margin_of_error *= np.count_nonzero(t * (time - t) > record)
    print(margin_of_error)


if __name__ == "__main__":
    main()
