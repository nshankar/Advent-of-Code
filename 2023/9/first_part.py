import numpy as np


def main():
    with open("input.txt", encoding="utf-8") as file:
        data = [line.strip() for line in file.readlines()]

    timeseries = [np.array(line.split(), dtype=np.int64) for line in data]
    predictions = []
    for series in timeseries:
        predictions.append(series[-1])
        while not np.all(series == 0):
            series = np.diff(series)
            predictions[-1] += series[-1]
    print(sum(predictions))


if __name__ == "__main__":
    main()
