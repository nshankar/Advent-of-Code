def is_valid_interval(interval, record):
    # Return True if the given interval could be a contiguous interval
    # of damaged springs else return False
    a, b = interval
    return set(record[a:b]) <= {"?", "#"}


# I would find the root of the slowness but alas the complexity is quintic!
def ways(record, ecc):
    # memo[i][j] counts the number of ways continguous groups of lengths of ecc[:i]
    # damaged springs can exist in record[:j] with the last damaged spring is
    # located at record[j-1]. This count must respect the data already in the record
    m, n = len(ecc), len(record)
    memo = [[0] * n for _ in range(m)]

    # Initialize memo[0][:] with all valid locations for the first contiguous group
    for j in range(ecc[0], n + 1):
        if is_valid_interval((j - ecc[0], j), record):
            if record[: j - ecc[0]].count("#") == 0:
                memo[0][j - 1] = 1

    for i in range(1, m):
        for j in range(sum(ecc[: i + 1]) + i, n + 1):
            if is_valid_interval((j - ecc[i], j), record):
                # Ensure there are no damaged springs between the current interval
                # and the most recent predecessor
                valid_predecessors = [
                    memo[i - 1][k]
                    for k in range(j - ecc[i] - 1)
                    if record[k + 1 : j - ecc[i]].count("#") == 0
                ]
                memo[i][j - 1] = sum(valid_predecessors)

    # Discard solutions that don't account for every damaged spring
    start = record.rfind("#") if record.rfind("#") >= 0 else 0
    # print(sum(memo[-1][start:]))
    return sum(memo[-1][start:])


def main():
    # additional test cases
    assert 4 == ways("?##?????###?", [3, 6])
    assert 7 == ways("??#??..??..", [3, 1])
    assert 9 == ways(".??..???#????", [1, 2, 1, 1])
    assert 6 == ways("#?#????????.?#.", [4, 1, 2, 1])

    with open("input.txt", encoding="utf-8") as file:
        data = [
            [line.split()[0], list(map(int, line.split()[1].split(",")))]
            for line in file.readlines()
        ]
    s = 0
    for record, ecc in data:
        # ecc: error correcting code
        s += ways(record, ecc)
    print(s)


if __name__ == "__main__":
    main()
