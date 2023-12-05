from bisect import bisect_right


def extract_data(almanac):
    seeds = map(int, almanac[0].split(":")[1].split())
    mappings = []
    for line in almanac[2:]:
        if ":" in line:
            mappings.append([])
        if line and line[0].isdigit():
            dest, source, length = map(int, line.split())
            # start, end, delta
            mappings[-1].append((source, source + length, dest - source))
    mappings = list(map(sorted, mappings))
    return seeds, mappings


def main():
    with open("input.txt", encoding="utf-8") as file:
        almanac = [line.strip() for line in file.readlines()]

    seeds, mappings = extract_data(almanac)
    locations = []
    for seed in seeds:
        for mapping in mappings:
            idx = bisect_right(mapping, (seed, float("inf"), 0))
            if idx == 0:
                continue
            start, end, delta = mapping[idx - 1]
            if seed >= start and seed < end:
                seed += delta
        locations.append(seed)
    print(min(locations))


if __name__ == "__main__":
    main()
