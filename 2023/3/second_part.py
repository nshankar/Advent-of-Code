from first_part import in_bounds
from math import prod


def get_full_number(data, row, col):
    start = col
    while start >= 0 and data[row][start].isdigit():
        start -= 1
    start += 1

    end = col
    while end < len(data[row]) and data[row][end].isdigit():
        end += 1

    return int(data[row][start:end]), start, end


def get_neighboring_numbers(data, row, col):
    numbers = []
    for i in range(row - 1, row + 2):
        skip_counter = 0
        for j in range(col - 1, col + 2):
            if skip_counter > 0:
                skip_counter -= 1
                continue
            if in_bounds(i, j, data):
                if data[i][j].isdigit():
                    number, _, end = get_full_number(data, i, j)
                    numbers.append(number)
                    skip_counter = end - j
    return numbers


def main():
    with open("input.txt", encoding="utf-8") as file:
        data = [line.strip() for line in file.readlines()]

    s = 0
    for row, line in enumerate(data):
        for col, char in enumerate(line):
            if char == "*":
                numbers = get_neighboring_numbers(data, row, col)
                if len(numbers) == 2:
                    s += prod(numbers)
    print(s)


if __name__ == "__main__":
    main()
