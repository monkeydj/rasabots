"""
This adheres a solution of Day 5 puzzle Part Two
- https://adventofcode.com/2023/day/5#part2

Some references for efficient range lookup:
- https://github.com/jonathanpaulson/AdventOfCode/blob/master/2023/5.py
- https://github.com/womogenes/AoC-2023-Solutions/blob/main/day_05/day_05_p2.py
"""

from sys import argv


def lookup(s_start: int, s_length: int, almanac: list[list[set]]) -> list[set]:
    locations = [[(s_start, s_start + s_length - 1)]]

    for dest_loc in almanac:
        locations.append([])  # in new map

        for dest_start, src_start, length in dest_loc:
            src_end = src_start + length - 1

            for start, end in locations[-2]:  # loop through src locations

                if start > src_end or end < src_start:
                    continue  # not in map

                junction_length = min(end, src_end) - max(s_start, src_start)

                mapped_start = dest_start + (s_start - src_start)
                mapped_end = mapped_start + junction_length - 1

                locations[-1].append((mapped_start, mapped_end))
            else:  # lookup is ended,
                # start checking the next map in almanac
                pass

    return locations[-1]  # very last collection is desired locations


seeds, *maps = open("test.in").read().split("\n\n")
# (it just changes the format of seed range, but the data amount is huge!)

# ideally, it just follow downstream to find seed's location:
# seed -> soil -> fertilizer -> water -> light -> temperature -> humidity -> location
almanac = []

# ? if the maps are not in order of downstream
for categories_map in maps:
    map_name, _, *ranges = categories_map.split()

    almanac.append([])  # try to make lookup easier

    for i in range(0, len(ranges), 3):  # always multiple of 3
        dest_start, src_start, length = map(int, ranges[i:(i + 3)])
        almanac[-1].append((dest_start, src_start, length))

        print(map_name, "/ map=", (dest_start, src_start, length))


seeds = [int(s) for s in seeds.split()[1:]]

for seed_start, seed_range in list(zip(seeds[::2], seeds[1::2])):

    print("seed_range=", f"({seed_start} + {seed_range})")

    locations = lookup(seed_start, seed_range, almanac)
    print(locations)

print(f"[Min Position Is: {0}]")
