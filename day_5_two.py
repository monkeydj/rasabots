"""
This adheres a solution of Day 5 puzzle Part Two
- https://adventofcode.com/2023/day/5#part2
"""

from sys import argv


def find_dest_pos(src_pos: int, dest_start: int, src_start: int, length: int) -> int:
    if src_start <= src_pos < src_start + length:
        return dest_start + (src_pos - src_start)

    return src_pos


seeds, *maps = open(argv[1]).read().split('\n\n')
# (it just changes the format of seed range, but the data amount is huge!)

# ideally, it just follow downstream to find seed's location:
# seed -> soil -> fertilizer -> water -> light -> temperature -> humidity -> location
downstream = []

# ? if the maps are not in order of downstream
for categories_map in maps:
    src_to_dest, _, *ranges = categories_map.split()

    for i in range(0, len(ranges), 3):  # always multiple of 3
        dest_start, src_start, length = map(int, ranges[i:(i + 3)])
        downstream.append((src_to_dest, (dest_start, src_start, length)))

        print(src_to_dest, "/ map=", (dest_start, src_start, length))

seed_ranges = list(map(int, seeds.split()[1:]))

for i in range(0, len(seed_ranges), 2):
    seed_start, seed_range = seed_ranges[i], seed_ranges[i + 1]

    print("seeds=", f"({seed_start} + {seed_range})")


answer = 0
print(f"[Total Score Is: {answer}]")
