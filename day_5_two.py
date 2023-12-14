"""
This adheres a solution of Day 5 puzzle Part Two
- https://adventofcode.com/2023/day/5#part2
"""

from sys import argv


def lookup(seed_pos: int, almanac: list[set]) -> int:
    position, prev_done_map = seed_pos, None

    for map_name, dest_start, src_start, length in almanac:
        if map_name == prev_done_map:
            continue
        # else it keeps checking the next map in almanac
        if src_start <= position < src_start + length:
            position = dest_start + (position - src_start)
            prev_done_map = map_name

    return position


seeds, *maps = open(argv[1]).read().split('\n\n')
# (it just changes the format of seed range, but the data amount is huge!)

# ideally, it just follow downstream to find seed's location:
# seed -> soil -> fertilizer -> water -> light -> temperature -> humidity -> location
almanac = []

# ? if the maps are not in order of downstream
for categories_map in maps:
    map_name, _, *ranges = categories_map.split()

    for i in range(0, len(ranges), 3):  # always multiple of 3
        dest_start, src_start, length = map(int, ranges[i:(i + 3)])
        almanac.append((map_name, dest_start, src_start, length))

        print(map_name, "/ map=", (dest_start, src_start, length))


seed_ranges, min_pos = seeds.split()[1:], float("inf")

for i in range(0, len(seed_ranges), 2):
    seed_start, seed_length = int(seed_ranges[i]), int(seed_ranges[i + 1])

    for seed in range(seed_start, seed_start + seed_length):
        min_pos = min(min_pos, lookup(seed, almanac))

    print("seeds=", f"({seed_start} + {seed_length})", "min_pos=", min_pos)

print(f"[Min Position Is: {min_pos}]")
