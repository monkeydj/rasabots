"""
This adheres a solution of Day 5 puzzle Part Two
- https://adventofcode.com/2023/day/5#part2
"""

from sys import argv


def find_dest_pos(src_pos: int, src_dest_ranges: list[int]) -> int:
    for i in range(0, len(src_dest_ranges), 3):  # always multiple of 3
        dest_start, src_start, length = map(int, src_dest_ranges[i:(i + 3)])

        if src_start <= src_pos < src_start + length:
            return dest_start + (src_pos - src_start)

    return src_pos


seeds, *maps = open(argv[1]).read().split('\n\n')
# (it just changes the format of seed range)
fst_start, fst_range, snd_start, snd_range = list(map(int, seeds.split()[1:]))
positions = (list(range(fst_start, fst_start + fst_range)) +
             list(range(snd_start, snd_start + snd_range)))

print("seeds=", positions)

# ideally, it just follow downstream to find seed's location:
# seed -> soil -> fertilizer -> water -> light -> temperature -> humidity -> location
for categories_map in maps:
    src_to_dest, _, *ranges = categories_map.split()
    # ? if the maps are not in order of downstream
    positions = [find_dest_pos(p, ranges) for p in positions]

    print(src_to_dest + "=", positions, "/ map=", ranges)

answer = min(positions)
print(f"[Total Score Is: {answer}]")
