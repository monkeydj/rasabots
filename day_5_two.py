"""
This adheres a solution of Day 5 puzzle Part Two
- https://adventofcode.com/2023/day/5#part2
"""

from sys import argv


def find_dest_pos(src_pos: int, src_dest_ranges: list[set]) -> int:
    for dest_start, src_start, length in src_dest_ranges:
        if src_start <= src_pos < src_start + length:
            return dest_start + (src_pos - src_start)

    return src_pos


seeds, *maps = open("test.in").read().split('\n\n')
# (it just changes the format of seed range, but the data amount is huge!)

# ideally, it just follow downstream to find seed's location:
# seed -> soil -> fertilizer -> water -> light -> temperature -> humidity -> location
downstream = []

# ? if the maps are not in order of downstream
for categories_map in maps:
    src_to_dest, _, *ranges = categories_map.split()

    for i in range(0, len(ranges), 3):  # always multiple of 3
        dest_start, src_start, length = map(int, ranges[i:(i + 3)])
        downstream.append((dest_start, src_start, length))

        print(src_to_dest, "/ map=", (dest_start, src_start, length))


seed_ranges, min_pos = seeds.split()[1:], float("inf")

for i in range(0, len(seed_ranges), 2):
    seed_start, seed_length = int(seed_ranges[i]), int(seed_ranges[i + 1])

    for seed in range(seed_start, seed_start + seed_length):
        min_pos = min(min_pos, find_dest_pos(seed, downstream))

    print("seeds=", f"({seed_start} + {seed_length})", "min_pos=", min_pos)

print(f"[Min Position Is: {min_pos}]")
