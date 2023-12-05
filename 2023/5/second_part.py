from bisect import bisect_right
from queue import SimpleQueue

INF = float("inf")


def extract_seeds(almanac):
    raw_data = map(int, almanac[0].split(":")[1].split())
    seed_ranges = SimpleQueue()
    for start in raw_data:
        length = next(raw_data)
        seed_ranges.put((start, start + length))

    return seed_ranges


def extract_mappings(almanac):
    mappings = []
    for line in almanac[2:]:
        if ":" in line:
            mappings.append([])
        if line and line[0].isdigit():
            dest, source, length = map(int, line.split())
            # start, end, delta
            mappings[-1].append((source, source + length, dest - source))
    mappings = list(map(sorted, mappings))
    return mappings


def helper(seed_range, alt_end, delta, seeds, new_seeds):
    # update Queue and new Queue
    seed_start, seed_end = seed_range
    new_seeds.put((seed_start + delta, min(seed_end, alt_end) + delta))
    if seed_end > alt_end:
        seeds.put((alt_end, seed_end))


def main():
    """
    Since working with individual seeds is unwieldy we instead work with intervals of seeds (a, b).
    For each layer of the mapping (seed-to-soil, soil-to-fertalizer, etc) pass all seed ranges through
    that layer by using a Queue and considering how the seed intervals and mapping intervals intersect.
    """
    with open("input.txt", encoding="utf-8") as file:
        almanac = [line.strip() for line in file.readlines()]

    seeds = extract_seeds(almanac)
    mappings = extract_mappings(almanac)
    for mapping in mappings:
        new_seeds = SimpleQueue()
        while not seeds.empty():
            seed_start, seed_end = seeds.get()
            idx = bisect_right(mapping, (seed_start, INF, 0))
            if idx == 0:
                _, mapping_end, _ = mapping[idx]
                delta = 0
                helper((seed_start, seed_end), mapping_end, delta, seeds, new_seeds)

            else:  # idx > 0
                _, mapping_end, delta = mapping[idx - 1]
                next_mapping_start, _, _ = (
                    mapping[idx] if idx < len(mapping) else (INF, None, None)
                )

                if seed_start < mapping_end:
                    final_delta = delta
                    alt_end = mapping_end
                else:
                    final_delta = 0
                    alt_end = next_mapping_start
                helper((seed_start, seed_end), alt_end, final_delta, seeds, new_seeds)

        seeds = new_seeds

    # Get minimum location
    minimum_location = (INF, 0)
    while not seeds.empty():
        minimum_location = min(minimum_location, seeds.get())
    print("Minimum location:", minimum_location[0])


if __name__ == "__main__":
    main()
