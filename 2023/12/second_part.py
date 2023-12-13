from first_part import ways


def unroll(record, ecc):
    return ((record + "?") * 5)[:-1], ecc * 5


def main():
    with open("input.txt", encoding="utf-8") as file:
        data = [
            [line.split()[0], list(map(int, line.split()[1].split(",")))]
            for line in file.readlines()
        ]
    s = 0
    for record, ecc in data:
        # ecc: error correcting code
        s += ways(*unroll(record, ecc))
    print(s)


if __name__ == "__main__":
    main()
