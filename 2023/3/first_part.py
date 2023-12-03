def len_number(s: str, start: int):
    length = 0
    while start < len(s) and s[start].isdigit():
        length += 1
        start += 1
    return length


def in_bounds(i, j, data):
    return i >= 0 and i < len(data) and j >= 0 and j < len(data[i])


def is_part_number(data, number_row, number_start_col, number_end_col):
    "Given data and the location of the number check whether any adjacent chars are symbols"
    for i in range(number_row - 1, number_row + 2):
        for j in range(number_start_col - 1, number_end_col + 1):
            if in_bounds(i, j, data):
                if not data[i][j].isdigit() and data[i][j] != ".":
                    return True
    return False


def main():
    with open("input.txt", encoding="utf-8") as file:
        data = [line.strip() for line in file.readlines()]

    s = 0
    for row, line in enumerate(data):
        # Use a skip counter to avoid double counting numbers
        skip_counter = 0
        for col, char in enumerate(line):
            if skip_counter > 0 or not char.isdigit():
                skip_counter -= 1
                continue
            length = len_number(line, col)
            if is_part_number(data, row, col, col + length):
                s += int(line[col : col + length])
            skip_counter = length

    print(s)


if __name__ == "__main__":
    main()
